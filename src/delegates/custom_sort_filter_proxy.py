from PySide6.QtCore import QSortFilterProxyModel
from sqlalchemy.sql.sqltypes import Integer, DateTime, String
from PySide6.QtCore import Qt
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class CustomSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.column_types = [
            Integer,      # id
            String,       # equipment_name
            String,       # equipment_type
            String,       # serial_number
            String,       # location
            Integer,      # calibration_interval
            DateTime,     # last_calibration_date
            DateTime,     # next_calibration_date
            String,       # certificate_number
            Integer,      # days_to_calibration
            String        # notes
        ]

    def lessThan(self, left, right):
        left_data = self.sourceModel().data(left, Qt.DisplayRole)
        right_data = self.sourceModel().data(right, Qt.DisplayRole)
        column = left.column()

        try:
            column_type = self.column_types[column]

            if left_data is None and right_data is None:
                return False
            if left_data is None:
                return True
            if right_data is None:
                return False

            if column_type == Integer:
                left_value = int(left_data) if left_data else 0
                right_value = int(right_data) if right_data else 0
                return left_value < right_value
            elif column_type == DateTime:
                left_value = datetime.strptime(left_data, '%d-%m-%Y') if left_data else datetime.min
                right_value = datetime.strptime(right_data, '%d-%m-%Y') if right_data else datetime.min
                return left_value < right_value
            else:
                left_value = str(left_data).lower() if left_data else ""
                right_value = str(right_data).lower() if right_data else ""
                return left_value < right_value
        except Exception as e:
            logger.error(f"Ошибка сортировки в колонке {column}: {str(e)}")
            return str(left_data).lower() < str(right_data).lower()