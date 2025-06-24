from PySide6.QtWidgets import QMessageBox
import logging
from ui.event_edit_dialog import EventEditDialog
from bd.calibration_event_model import CalibrationEvent

logger = logging.getLogger(__name__)

def create_event(window):
    logger.debug("Создание нового события")
    new_event = CalibrationEvent()
    dialog = EventEditDialog(new_event, window.event_model, window)
    if dialog.exec():
        try:
            window.session_manager.add(new_event)
            window.session_manager.commit()
            logger.debug("Новое событие добавлено")
            window.last_selected_event_row = None
            window.event_model.refresh()
            window.model.refresh()
            window.ui.eventTableView.resizeRowsToContents()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка сохранения события: {str(e)}")
            window.show_error("Ошибка", f"Ошибка сохранения события: {str(e)}")

def edit_event(window):
    if not window.current_calibration_event:
        window.show_error("Ошибка", "Выберите событие для редактирования")
        return
    dialog = EventEditDialog(window.current_calibration_event, window.event_model, window)
    if dialog.exec():
        try:
            window.session_manager.commit()
            logger.debug("Событие обновлено")
            window.last_selected_event_row = None
            window.event_model.refresh()
            window.model.refresh()
            window.ui.eventTableView.resizeRowsToContents()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка сохранения события: {str(e)}")
            window.show_error("Ошибка", f"Ошибка сохранения события: {str(e)}")

def delete_event(window):
    if not window.current_calibration_event:
        window.show_error("Ошибка", "Выберите событие для удаления")
        return

    reply_box = QMessageBox(window)
    reply_box.setIcon(QMessageBox.Question)
    reply_box.setWindowTitle("Подтверждение удаления")
    reply_box.setText(f"Удалить событие с {window.current_calibration_event.check_days} днями до проверки?")
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

    if reply == QMessageBox.Yes:
        try:
            window.session_manager.delete(window.current_calibration_event)
            window.session_manager.commit()
            logger.debug("Событие удалено")
            window.current_calibration_event = None
            window.last_selected_event_row = None
            window.event_model.refresh()
            window.model.refresh()
            window.ui.eventTableView.resizeRowsToContents()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка при удалении события: {str(e)}")
            window.show_error("Ошибка", f"Ошибка при удалении события: {str(e)}")