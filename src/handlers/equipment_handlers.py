from PySide6.QtWidgets import QMessageBox
from sqlalchemy import DateTime, Integer, String, inspect
import logging
from ui.equipment_edit_dialog import EquipmentEditDialog
from bd.equipment_model import Equipment
from datetime import date, datetime, timedelta
from PySide6.QtWidgets import QHeaderView

logger = logging.getLogger(__name__)

def process_equipment_data(window, equipment, data, table_columns):
    inspector = inspect(window.session_manager.bind)
    for key, value in data.items():
        if key in table_columns:
            try:
                col_type = next(col['type'] for col in inspector.get_columns('equipment') if col['name'] == key)
                logger.debug(f"Обработка поля {key}: value={value}, type={type(value)}, col_type={col_type}")
                processed_value = None
                if value is not None:
                    if isinstance(col_type, Integer):
                        try:
                            processed_value = int(value) if isinstance(value, str) else value
                        except (ValueError, TypeError):
                            logger.warning(f"Некорректное значение для {key}: {value}")
                            processed_value = None
                    elif isinstance(col_type, DateTime):
                        if isinstance(value, str):
                            try:
                                processed_value = datetime.strptime(value, '%Y-%m-%d')
                            except ValueError:
                                logger.error(f"Ошибка парсинга даты для {key}: {value}")
                                raise ValueError(f"Некорректный формат даты для {key}: ожидается ГГГГ-ММ-ДД")
                        elif isinstance(value, date):
                            processed_value = datetime.combine(value, datetime.min.time())
                        elif isinstance(value, datetime):
                            processed_value = value
                        else:
                            logger.warning(f"Некорректный тип для {key}: {type(value)}")
                            processed_value = None
                    elif isinstance(col_type, String):
                        processed_value = str(value).strip() if value else None
                    else:
                        processed_value = value
                setattr(equipment, key, processed_value)
                logger.debug(f"Установлено значение: {key} = {processed_value}")
            except Exception as e:
                logger.error(f"Ошибка установки {key}: {str(e)}")
                raise

def create_equipment(window):
    logger.debug("Создание новой записи оборудования")
    new_equipment = Equipment()
    dialog = EquipmentEditDialog(new_equipment, window.model, window)
    if dialog.exec():
        data = dialog.get_data()
        logger.debug(f"Данные из диалога: {data}")
        table_columns = {col["name"] for col in inspect(window.session_manager.bind).get_columns('equipment')}
        logger.debug(f"Колонки таблицы: {table_columns}")
        try:
            process_equipment_data(window, new_equipment, data, table_columns)
            new_equipment.update_calibration()
            window.session_manager.add(new_equipment)
            window.session_manager.commit()
            logger.debug(f"Новая запись создана: {new_equipment.equipment_name}")
            window.last_selected_row = None
            window.last_selected_event_row = None
            window.model.refresh()
            window.ui.tableView.resizeRowsToContents()
            window.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            window.adjust_column_widths()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка при сохранении записи: {str(e)}")
            window.show_error("Ошибка", f"Ошибка при сохранении записи: {str(e)}")

def edit_equipment(window):
    if not window.current_equipment:
        window.show_error("Ошибка", "Выберите запись для редактирования")
        return
    dialog = EquipmentEditDialog(window.current_equipment, window.model, window)
    if dialog.exec():
        data = dialog.get_data()
        logger.debug(f"Данные из редактирования: {data}")
        table_columns = {col["name"] for col in inspect(window.session_manager.bind).get_columns('equipment')}
        logger.debug(f"Колонки таблицы: {table_columns}")
        try:
            process_equipment_data(window, window.current_equipment, data, table_columns)
            window.current_equipment.update_calibration()
            window.session_manager.commit()
            logger.debug(f"Запись обновлена: {window.current_equipment.equipment_name}")
            window.last_selected_row = None
            window.last_selected_event_row = None
            window.model.refresh()
            window.ui.tableView.resizeRowsToContents()
            window.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            window.adjust_column_widths()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка при сохранении записи: {str(e)}")
            window.show_error("Ошибка", f"Ошибка при сохранении записи: {str(e)}")

def delete_equipment(window):
    if not window.current_equipment:
        window.show_error("Ошибка", "Выберите запись для удаления")
        return

    reply_box = QMessageBox(window)
    reply_box.setIcon(QMessageBox.Question)
    reply_box.setWindowTitle("Подтверждение удаления")
    reply_box.setText(f"Удалить запись '{window.current_equipment.equipment_name}'?")
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
            window.session_manager.delete(window.current_equipment)
            window.session_manager.commit()
            logger.debug(f"Запись удалена: {window.current_equipment.equipment_name}")
            window.current_equipment = None
            window.last_selected_row = None
            window.last_selected_event_row = None
            window.model.refresh()
            window.ui.tableView.resizeRowsToContents()
            window.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            window.adjust_column_widths()
            window.apply_sorting()
        except Exception as e:
            window.session_manager.rollback()
            logger.error(f"Ошибка при удалении записи: {str(e)}")
            window.show_error("Ошибка", f"Ошибка при удалении записи: {str(e)}")

def mark_verification_today(window):
    if not window.current_equipment:
        logger.error("Не выбрано оборудование для отметки поверки")
        window.show_error("Ошибка", "Выберите оборудование для отметки поверки")
        return

    try:
        today = datetime.now().date()
        logger.debug(f"Установка даты поверки для '{window.current_equipment.equipment_name}' (ID: {window.current_equipment.id}): {today}")

        if not hasattr(window.current_equipment, 'last_calibration_date'):
            logger.error("Поле 'lastCalibration_date' не найдено в модели Equipment")
            raise AttributeError("Поле 'last_calibration_date' отсутствует в модели")

        window.current_equipment.last_calibration_date = today
        logger.debug(f"Установлено last_calibration_date: {today}")

        if hasattr(window.current_equipment, 'calibration_interval') and window.current_equipment.calibration_interval is not None:
            try:
                interval_days = int(window.current_equipment.calibration_interval)
                logger.debug(f"Интервал поверки: {interval_days} дней")
                next_calibr_date = today + timedelta(days=interval_days)
                days_to_cal = interval_days

                if hasattr(window.current_equipment, 'next_calibration_date'):
                    window.current_equipment.next_calibration_date = next_calibr_date
                    logger.debug(f"Установлено next_calibration_date: {next_calibr_date}")

                if hasattr(window.current_equipment, 'days_to_calibration'):
                    window.current_equipment.days_to_calibration = days_to_cal
                    logger.debug(f"Установлено days_to_calibration: {days_to_cal}")
            except ValueError as ve:
                logger.error(f"Некорректный calibration_interval: {window.current_equipment.calibration_interval}")
                raise ValueError(f"Некорректный интервал поверки: {str(ve)}")

        window.session_manager.commit()
        logger.info(f"Поверка успешно сохранена для '{window.current_equipment.equipment_name}': last_calibration_date={today}")

        window.model.refresh()
        window.ui.tableView.resizeRowsToContents()
        window.apply_sorting()

        QMessageBox.information(window, "Успех", f"Поверка для '{window.current_equipment.equipment_name}' отмечена на {today.strftime('%d-%m-%Y')}")
    except ValueError as ve:
        window.session_manager.rollback()
        logger.error(f"Ошибка значения при отметке поверки: {str(ve)}")
        window.show_error("Ошибка", f"Ошибка значения: {str(ve)}")
    except Exception as e:
        window.session_manager.rollback()
        logger.error(f"Неизвестная ошибка при отметке поверки: {str(e)}")
        window.show_error("Ошибка", f"Неизвестная ошибка: {str(e)}")