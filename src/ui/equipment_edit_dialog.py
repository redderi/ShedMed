import logging
import re
from datetime import date, datetime
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QDateEdit, QMessageBox, QComboBox, QWidget, QCompleter
)
from PySide6.QtCore import Qt, QDate
from sqlalchemy import inspect

from bd.equipment_model import Equipment


logger = logging.getLogger(__name__)

class EquipmentEditDialog(QDialog):
    def __init__(self, equipment, model, parent=None):
        super().__init__(parent)
        self.equipment = equipment
        self.model = model
        self.session = model.session
        self.setWindowTitle("Редактировать оборудование" if equipment.id else "Добавить оборудование")
        self.setMinimumWidth(400)
        self.setStyleSheet("""
            QDialog {
                font: 10pt "Segoe UI";
                color: #333333;
            }
            QLabel {
                color: #333333;
                font: bold 10pt "Segoe UI";
                padding: 4px;
            }
            QLineEdit, QDateEdit, QComboBox {
                background-color: #FFFFFF;
                border: 1px solid #B0B0B0;
                border-radius: 6px;
                padding: 4px;
                color: #333333;
                font: 10pt "Segoe UI";
                min-height: 20px;
            }
            QLineEdit:focus, QDateEdit:focus, QComboBox:focus {
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

            /* Исправления для календаря */
            QCalendarWidget QWidget {
                background-color: #FFFFFF;
                color: #333333;
            }
            QCalendarWidget QToolButton {
                color: #333333;
                font-weight: bold;
            }
            QCalendarWidget QMenu {
                background-color: #FFFFFF;
                color: #333333;
            }
            QCalendarWidget QSpinBox {
                color: #333333;
                background-color: #FFFFFF;
            }
            QCalendarWidget QAbstractItemView {
                selection-background-color: #4A90E2;
                selection-color: white;
                color: #333333;
                background-color: #FFFFFF;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)
        self.inputs = {}

        try:
            inspector = inspect(self.session.bind)
            columns = inspector.get_columns('equipment')

            for column in columns:
                column_name = column['name']
                if column_name in ('id', 'next_calibration_date', 'days_to_calibration'):
                    continue

                display_name = self.model.DISPLAY_NAMES.get(
                    column_name, column_name.replace('_', ' ').title()
                )
                logger.debug(f"Колонка {column_name}: отображаемое имя = {display_name}")
                if column_name in ('equipment_name', 'last_calibration_date'):
                    display_name += ' *'
                label = QLabel(display_name)

                value = getattr(self.equipment, column_name, None)

                if column_name == 'last_calibration_date':
                    input_widget = QDateEdit()
                    input_widget.setCalendarPopup(True)
                    input_widget.setDisplayFormat("yyyy-MM-dd")
                    input_widget.setAlignment(Qt.AlignCenter)
                    input_widget.setToolTip("Выберите дату последней поверки")
                    if value:
                        try:
                            if isinstance(value, datetime):
                                input_widget.setDate(QDate(value.year, value.month, value.day))
                            elif isinstance(value, date):
                                input_widget.setDate(QDate(value.year, value.month, value.day))
                            else:
                                input_widget.setDate(QDate.currentDate())
                        except (AttributeError, TypeError):
                            input_widget.setDate(QDate.currentDate())
                    else:
                        input_widget.setDate(QDate.currentDate())

                elif column_name == 'calibration_interval':
                    interval_widget = QWidget()
                    interval_layout = QHBoxLayout(interval_widget)
                    interval_layout.setContentsMargins(0, 0, 0, 0)
                    interval_layout.setSpacing(8)

                    combo_widget = QComboBox()
                    combo_widget.setToolTip("Выберите интервал калибровки")
                    intervals = [
                        ("1 раз в 6 месяцев", 183),
                        ("1 раз в год", 365),
                        ("1 раз в 2 года", 730),
                        ("1 раз в 5 лет", 1825),
                    ]
                    combo_widget.addItem("Выберите интервал", userData=None)
                    for label_text, days in intervals:
                        combo_widget.addItem(label_text, userData=days)

                    days_widget = QLineEdit()
                    days_widget.setPlaceholderText("Дни")
                    days_widget.setAlignment(Qt.AlignCenter)
                    days_widget.setToolTip("Введите количество дней вручную")
                    days_widget.setMaximumWidth(100)

                    if value is not None:
                        found_index = -1
                        for i in range(combo_widget.count()):
                            data_days = combo_widget.itemData(i)
                            if data_days is not None and abs(data_days - value) < 1e-3:
                                found_index = i
                                break
                        if found_index >= 0:
                            combo_widget.setCurrentIndex(found_index)
                            days_widget.setText(str(int(value)))
                        else:
                            combo_widget.setCurrentIndex(0)  
                            days_widget.setText(str(int(value)))
                    else:
                        combo_widget.setCurrentIndex(0)
                        days_widget.setText("")

                    combo_widget.currentIndexChanged.connect(
                        lambda: self.on_interval_combo_changed(combo_widget, days_widget)
                    )
                    days_widget.textChanged.connect(
                        lambda: self.on_days_text_changed(combo_widget, days_widget)
                    )

                    interval_layout.addWidget(combo_widget)
                    interval_layout.addWidget(days_widget)

                    input_widget = interval_widget
                    self.inputs['calibration_interval_combo'] = combo_widget
                    self.inputs['calibration_interval_days'] = days_widget

                else:
                    input_widget = QLineEdit()
                    input_widget.setAlignment(Qt.AlignCenter)
                    if value is not None:
                        input_widget.setText(str(value))
                    if column_name == 'equipment_name':
                        input_widget.setPlaceholderText("Обязательное поле")
                    else:
                        input_widget.setPlaceholderText("")

                self.layout.addWidget(label)
                self.layout.addWidget(input_widget)
                self.inputs[column_name] = input_widget

            button_layout = QHBoxLayout()
            button_layout.setSpacing(8)
            save_button = QPushButton("Сохранить")
            cancel_button = QPushButton("Отмена")
            cancel_button.setObjectName("cancelButton")

            save_button.clicked.connect(self.validate_and_accept)
            cancel_button.clicked.connect(self.reject)

            button_layout.addStretch()
            button_layout.addWidget(save_button)
            button_layout.addWidget(cancel_button)

            self.layout.addSpacing(10)
            self.layout.addLayout(button_layout)

        except Exception as e:
            logger.error(f"Ошибка инициализации диалога: {str(e)}")
            raise

    def on_interval_combo_changed(self, combo_widget, days_widget):
        current_index = combo_widget.currentIndex()
        days = combo_widget.itemData(current_index)
        if days is not None:
            days_widget.setText(str(int(days)))
        else:
            if not days_widget.text().strip():
                days_widget.setText("")

    def on_days_text_changed(self, combo_widget, days_widget):
        text = days_widget.text().strip()
        if text:
            combo_widget.setCurrentIndex(0)  

    def validate_and_accept(self):
        try:
            data = self.get_data()
        except Exception as e:
            logger.error(f"Ошибка получения данных: {str(e)}")
            QMessageBox.critical(self, "Ошибка", f"Ошибка получения данных: {str(e)}")
            return

        if not data.get('equipment_name') or not data['equipment_name'].strip():
            QMessageBox.critical(self, "Ошибка", "Поле 'Название оборудования' обязательно для заполнения")
            logger.warning("Валидация не пройдена: пустое поле equipment_name")
            return

        if not data.get('last_calibration_date'):
            QMessageBox.critical(self, "Ошибка", "Поле 'Дата последней калибровки' обязательно для заполнения")
            logger.warning("Валидация не пройдена: пустое поле last_calibration_date")
            return

        if data.get('calibration_interval') is None:
            QMessageBox.critical(self, "Ошибка", "Поле 'Интервал калибровки' обязательно для заполнения")
            logger.warning("Валидация не пройдена: пустое поле calibration_interval")
            return

        if data.get('calibration_interval') <= 0:
            QMessageBox.critical(self, "Ошибка", "Интервал калибровки должен быть положительным числом")
            logger.warning("Валидация не пройдена: неположительный calibration_interval")
            return

        self.accept()

    def get_data(self):
        data = {}

        for column_name, widget in self.inputs.items():
            if isinstance(widget, QDateEdit):
                date_value = widget.date().toPython()
                try:
                    if isinstance(date_value, date):
                        date_value = datetime.combine(date_value, datetime.min.time())
                    data[column_name] = date_value
                except Exception as e:
                    logger.error(f"Ошибка преобразования даты для {column_name}: {str(e)}")
                    raise

            elif column_name == 'calibration_interval':
                days_text = self.inputs['calibration_interval_days'].text().strip()
                if days_text:
                    match = re.search(r'^\d+$', days_text)
                    if match:
                        data['calibration_interval'] = int(days_text)
                    else:
                        raise ValueError(f"Некорректное значение для интервала калибровки: '{days_text}'")
                else:
                    data['calibration_interval'] = None

            elif column_name not in ('calibration_interval_combo', 'calibration_interval_days'):
                text = widget.text().strip()
                data[column_name] = text if text else None

            if column_name not in ('calibration_interval_combo', 'calibration_interval_days'):
                logger.debug(f"Поле {column_name}: значение={data.get(column_name)}, тип={type(data.get(column_name))}")

        logger.debug(f"Данные из диалога: {data}")
        return data