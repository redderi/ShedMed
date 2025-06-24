import logging
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit,
    QPushButton, QColorDialog, QMessageBox
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

from bd.calibration_event_model import CalibrationEvent


logger = logging.getLogger(__name__)

class EventEditDialog(QDialog):
    def __init__(self, calibration_event: CalibrationEvent, model, parent=None):
        super().__init__(parent)
        self.calibration_event = calibration_event
        self.model = model
        self.setWindowTitle("Редактировать событие")
        self.setFixedSize(400, 280)
        self._color = QColor(self.calibration_event.highlight_color or "#00FF00")
        self.setStyleSheet("""
            QDialog {
                font: 10pt "Segoe UI";
                color: #333333;
            }
            QLabel {
                color: #333333;
                font: 10pt "Segoe UI";
                padding: 8px;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #B0B0B0;
                border-radius: 6px;
                padding: 8px;
                color: #333333;
                font: 10pt "Segoe UI";
                min-height: 36px;
            }
            QLineEdit:focus {
                border: 1px solid #4A90E2;
                background-color: #F9FAFB;
            }
            QLineEdit::placeholder {
                color: #999999;
            }
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 10px;
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
            QPushButton#colorButton {
                border: 1px solid #B0B0B0;
                border-radius: 6px;
                padding: 8px;
                min-width: 80px;
                min-height: 36px;
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignCenter)
        form_layout.setHorizontalSpacing(20)
        form_layout.setVerticalSpacing(12)

        self.check_days_edit = QLineEdit(str(self.calibration_event.check_days or ""))
        self.check_days_edit.setPlaceholderText("Введите количество дней")
        self.check_days_edit.setAlignment(Qt.AlignCenter)
        form_layout.addRow("Дни до поверки:", self.check_days_edit)

        self.color_button = QPushButton()
        self.color_button.setObjectName("colorButton")
        self.color_button.setFixedSize(80, 36)
        self._update_color_button_style()
        self.color_button.clicked.connect(self.choose_color)
        form_layout.addRow("Цвет подсветки:", self.color_button)

        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)
        button_layout.addStretch(1)

        save_button = QPushButton("Сохранить")
        save_button.setFixedWidth(100)
        save_button.clicked.connect(self.save)
        save_button.setDefault(True)

        cancel_button = QPushButton("Отмена")
        cancel_button.setObjectName("cancelButton")
        cancel_button.setFixedWidth(100)
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

    def _update_color_button_style(self):
        self.color_button.setStyleSheet(
            f"""
            QPushButton#colorButton {{
                background-color: {self._color.name()};
                border: 1px solid #B0B0B0;
                border-radius: 6px;
                padding: 8px;
                min-width: 80px;
                min-height: 36px;
            }}
            """
        )

    def choose_color(self):
        color = QColorDialog.getColor(self._color, self, "Выберите цвет")
        if color.isValid():
            self._color = color
            self._update_color_button_style()

    def save(self):
        try:
            check_days_text = self.check_days_edit.text().strip()
            if not check_days_text:
                QMessageBox.critical(self, "Ошибка", "Заполните поле 'Дни до проверки'")
                return

            check_days = int(check_days_text)
            if check_days < 0:
                QMessageBox.critical(self, "Ошибка", "Значение не может быть отрицательным")
                return

            self.calibration_event.check_days = check_days
            self.calibration_event.highlight_color = self._color.name()
            self.accept()

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите числовое значение для дней")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")