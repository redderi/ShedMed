from datetime import datetime
import logging
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from sqlalchemy import inspect

from bd.equipment_model import Equipment


logger = logging.getLogger(__name__)

class EquipmentInfoDialog(QDialog):
    def __init__(self, equipment, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.equipment = model.session.query(Equipment).get(equipment.id)
        if not self.equipment:
            logger.error(f"Оборудование с ID {equipment.id} не найдено")
            raise ValueError(f"Оборудование с ID {equipment.id} не найдено")

        self.setWindowTitle(f"Информация об оборудовании: {self.equipment.equipment_name}")
        self.setMinimumWidth(400)
        self.setStyleSheet("""
            QDialog {
                background-color: #F5F6F5;
                font: 10pt "Segoe UI";
                color: #333333;
            }
            QLabel {
                color: #333333;
                font: 10pt "Segoe UI";
                padding: 4px;
                background-color: #FFFFFF;
                border: 1px solid #D3D3D3;
                border-radius: 6px;
                margin: 4px;
            }
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #4A90E2, stop:1 #357ABD);
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 10px;
                font: bold 10pt "Segoe UI";
                min-width: 100px;
                min-height: 25px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #357ABD, stop:1 #2D5D9F);
            }
            QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2D5D9F, stop:1 #254C80);
            }
            QPushButton:disabled {
                background-color: #CCCCCC;
                color: #666666;
            }
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)

        try:
            inspector = inspect(self.model.session.bind)
            columns = inspector.get_columns('equipment')

            for column in columns:
                column_name = column['name']
                if column_name == 'id':
                    continue 

                display_name = self.model.DISPLAY_NAMES.get(
                    column_name, column_name.replace('_', ' ').title()
                )
                value = getattr(self.equipment, column_name, None)
                if isinstance(value, datetime):
                    value = value.strftime('%d-%m-%Y')
                elif value is None:
                    value = ""

                label = QLabel(f"<b>{display_name}:</b><br>{value}")
                label.setAlignment(Qt.AlignLeft)
                label.setWordWrap(True)  
                self.layout.addWidget(label)

            close_button = QPushButton("Закрыть")
            close_button.clicked.connect(self.accept)
            self.layout.addWidget(close_button, alignment=Qt.AlignCenter)

        except Exception as e:
            logger.error(f"Ошибка инициализации диалога: {str(e)}")
            raise