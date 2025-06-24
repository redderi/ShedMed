import logging
import shutil
import os
from datetime import datetime
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt

from utils.path_utils import get_database_path


logger = logging.getLogger(__name__)

class BackupsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Резервное копирование базы данных")
        self.setFixedSize(320, 280)

        self.setStyleSheet("""
            QDialog {
                background-color: #F5F6F5;
                font: 10pt "Segoe UI";
                color: #333333;
            }
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 12px;
                margin: 6px;
                font: bold 10pt "Segoe UI";
                min-width: 100px;
                min-height: 36px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);
            }
            QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);
            }
            QPushButton#cancelButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #E24A4A, stop:1 #BD3535);
            }
            QPushButton#cancelButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #BD3535, stop:1 #9F2D2D);
            }
            QPushButton#cancelButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #9F2D2D, stop:1 #802525);
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
            }
        """)

        self.db_path = get_database_path()
        self.backup_dir = os.path.dirname(self.db_path)
        if not os.path.exists(self.backup_dir):
            QMessageBox.critical(self, "Ошибка", f"Директория с базой данных не найдена: {self.backup_dir}")
            self.reject()
            return

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        self.save_button = QPushButton("Сохранить базу данных")
        self.load_button = QPushButton("Загрузить базу данных")
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setObjectName("cancelButton")

        for btn in (self.save_button, self.load_button, self.cancel_button):
            btn.setMinimumHeight(36)
            btn.setCursor(Qt.PointingHandCursor)

        self.save_button.clicked.connect(self.save_database)
        self.load_button.clicked.connect(self.load_database)
        self.cancel_button.clicked.connect(self.reject)

        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.cancel_button)
        layout.addStretch()

    def save_database(self):
        logger.debug("Вызван метод save_database")
        try:
            if not os.path.exists(self.db_path):
                logger.error(f"База данных не найдена: {self.db_path}")
                self.show_error("Ошибка", f"База данных не найдена: {self.db_path}")
                return

            if not os.path.exists(self.backup_dir):
                os.makedirs(self.backup_dir)
                logger.debug(f"Создана директория для резервных копий: {self.backup_dir}")
            self.parent().session_manager.commit()
            logger.debug("Все изменения в сессии сохранены перед созданием резервной копии")

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            default_name = os.path.join(self.backup_dir, f"backup_{timestamp}.db")

            file_name, _ = QFileDialog.getSaveFileName(
                self, "Сохранить базу данных", default_name, "SQLite Database (*.db)"
            )
            if file_name:
                if not file_name.endswith('.db'):
                    file_name += '.db'
                    logger.debug(f"Добавлено расширение .db к имени файла: {file_name}")

                shutil.copy2(self.db_path, file_name)
                logger.info(f"База данных сохранена в {file_name}")

                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Успех")
                msg_box.setText(f"База данных сохранена в {file_name}")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.setStyleSheet("""
                    QMessageBox {
                        background-color: #ffffff;
                        font-size: 14px;
                        color: #000000;
                    }
                    QLabel {
                        color: #000000;
                    }
                    QPushButton {
                        min-width: 80px;
                        padding: 6px 12px;
                        color: #000000;
                        background-color: #f0f0f0;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                    }
                    QPushButton:hover {
                        background-color: #0078d7;
                        color: white;
                    }
                    QPushButton:pressed {
                        background-color: #005a9e;
                    }
                """)
                msg_box.exec()
                self.accept()

        except Exception as e:
            logger.error(f"Ошибка сохранения базы данных: {str(e)}")
            self.show_error("Ошибка", f"Ошибка сохранения: {str(e)}")

    def load_database(self):
        logger.debug("Вызван метод load_database")
        try:
            reply_box = QMessageBox(self)
            reply_box.setIcon(QMessageBox.Question)
            reply_box.setWindowTitle("Подтверждение")
            reply_box.setText("Загрузка новой базы данных заменит текущую. Продолжить?")
            reply_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            reply_box.setDefaultButton(QMessageBox.No)
            reply_box.setStyleSheet("""
                QMessageBox {
                    background-color: #ffffff;
                    font-size: 14px;
                    color: #000000;
                }
                QLabel {
                    color: #000000;
                }
                QPushButton {
                    min-width: 80px;
                    padding: 6px 12px;
                    color: #000000;
                    background-color: #f0f0f0;
                    border: 1px solid #cccccc;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #0078d7;
                    color: white;
                }
                QPushButton:pressed {
                    background-color: #005a9e;
                }
            """)
            reply = reply_box.exec()

            if reply != QMessageBox.Yes:
                logger.debug("Загрузка базы данных отменена пользователем")
                return

            file_name, _ = QFileDialog.getOpenFileName(
                self, "Загрузить базу данных", self.backup_dir, "SQLite Database (*.db)"
            )
            if file_name:
                if file_name == self.db_path:
                    logger.warning("Выбранный файл совпадает с текущей базой данных")
                    self.show_error("Ошибка", "Нельзя загрузить текущую базу данных")
                    return

                if not os.path.exists(file_name):
                    logger.error(f"Файл не найден: {file_name}")
                    self.show_error("Ошибка", f"Файл не найден: {file_name}")
                    return
                
                self.parent().session_manager.close()
                self.parent().db_manager.close()
                logger.debug("Текущая сессия и соединение закрыты")

                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_path = os.path.join(self.backup_dir, f"pre_load_backup_{timestamp}.db")
                if os.path.exists(self.db_path):
                    shutil.copy2(self.db_path, backup_path)
                    logger.debug(f"Создано резервное копие текущей базы: {backup_path}")

                shutil.copy2(file_name, self.db_path)
                logger.info(f"База данных загружена из {file_name} в {self.db_path}")

                self.parent().session_manager = self.parent().db_manager.get_session()
                self.parent().model.session = self.parent().session_manager
                self.parent().event_model.session = self.parent().session_manager
                self.parent().model.refresh()
                self.parent().event_model.refresh()
                self.parent().apply_sorting()
                self.parent().ui.tableView.resizeRowsToContents()
                self.parent().ui.eventTableView.resizeRowsToContents()
                logger.debug("Сессия и модели обновлены")

                msg_box = QMessageBox(self)
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Успех")
                msg_box.setText(f"База данных загружена из {file_name}")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.setStyleSheet("""
                    QMessageBox {
                        background-color: #ffffff;
                        font-size: 14px;
                        color: #000000;
                    }
                    QLabel {
                        color: #000000;
                    }
                    QPushButton {
                        min-width: 80px;
                        padding: 6px 12px;
                        color: #000000;
                        background-color: #f0f0f0;
                        border: 1px solid #cccccc;
                        border-radius: 4px;
                    }
                    QPushButton:hover {
                        background-color: #0078d7;
                        color: white;
                    }
                    QPushButton:pressed {
                        background-color: #005a9e;
                    }
                """)
                msg_box.exec()
                self.accept()

        except Exception as e:
            logger.error(f"Ошибка загрузки базы данных: {str(e)}")
            self.show_error("Ошибка", f"Ошибка загрузки: {str(e)}")
            try:
                self.parent().session_manager = self.parent().db_manager.get_session()
                self.parent().model.session = self.parent().session_manager
                self.parent().event_model.session = self.parent().session_manager
                self.parent().model.refresh()
                self.parent().event_model.refresh()
                self.parent().apply_sorting()
                logger.debug("Сессия восстановлена после ошибки")
            except Exception as e2:
                logger.error(f"Ошибка восстановления сессии: {str(e2)}")
                self.show_error("Критическая ошибка", f"Не удалось восстановить сессию: {str(e2)}")

    def show_error(self, title, message):
        logger.error(f"{title}: {message}")
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle(title)
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.setDefaultButton(QMessageBox.Ok)
        error_box.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
                color: #000000;
                font-size: 14px;
                font-family: Segoe UI, sans-serif;
                padding: 12px;
            }
            QPushButton {
                background-color: #d64541;
                color: white;
                padding: 6px 12px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        error_box.setWindowFlags(error_box.windowFlags() | Qt.WindowStaysOnTopHint)
        error_box.exec()