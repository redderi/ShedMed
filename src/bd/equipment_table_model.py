import logging
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtGui import QColor
from sqlalchemy.orm import Session

from bd.equipment_model import Equipment
from bd.calibration_event_model import CalibrationEvent


logger = logging.getLogger(__name__)

class EquipmentTableModel(QAbstractTableModel):
    DISPLAY_NAMES = {
        "equipment_name": "Наименование СИ (медицинское оборудование)",
        "equipment_type": "Тип, марка",
        "serial_number": "Заводской номер",
        "location": "Место нахождения",
        "calibration_interval": "Межповерочный интервал",
        "last_calibration_date": "Дата поверки",
        "next_calibration_date": "Дата следующей поверки",
        "certificate_number": "№ свидетельства о государственной поверке или аттестата",
        "days_to_calibration": "Количество дней до поверки",
        "notes": "Примечания"
    }
    COLUMN_MAPPING = {"Все колонки": None, **{v: k for k, v in DISPLAY_NAMES.items()}}
    HEADERS = ["Номер"] + list(DISPLAY_NAMES.values())

    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.all_equipments = []
        self.equipments = []
        self.events = []
        self.headers = self.HEADERS
        self._is_resetting = False 
        self.refresh()

    def rowCount(self, parent=QModelIndex()):
        return len(self.equipments)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        try:
            equipment = self.equipments[index.row()]
            column = index.column()

            if role == Qt.DisplayRole:
                if column == 0:
                    return str(index.row() + 1)
                elif column == 1:
                    return equipment.equipment_name
                elif column == 2:
                    return equipment.equipment_type
                elif column == 3:
                    return equipment.serial_number
                elif column == 4:
                    return equipment.location
                elif column == 5:
                    return str(equipment.calibration_interval) if equipment.calibration_interval is not None else ""
                elif column == 6:
                    return equipment.last_calibration_date.strftime('%d-%m-%Y') if equipment.last_calibration_date else ""
                elif column == 7:
                    return equipment.next_calibration_date.strftime('%d-%m-%Y') if equipment.next_calibration_date else ""
                elif column == 8:
                    return equipment.certificate_number if equipment.certificate_number else ""
                elif column == 9:
                    return str(equipment.days_to_calibration) if equipment.days_to_calibration is not None else ""
                elif column == 10:
                    return equipment.notes if equipment.notes else ""
            elif role == Qt.BackgroundRole:
                if equipment.days_to_calibration is not None:
                    for event in self.events:
                        if equipment.days_to_calibration <= event.check_days:
                            return QColor(event.highlight_color)
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
        except Exception as e:
            logger.error(f"Ошибка в методе data: {str(e)}")
            return None
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None

    def refresh(self):
        if self._is_resetting:
            return
        try:
            self._is_resetting = True
            self.beginResetModel()
            self.all_equipments = self.session.query(Equipment).order_by(Equipment.id).all()
            self.events = self.session.query(CalibrationEvent).order_by(CalibrationEvent.id).all()
            self.equipments = self.all_equipments[:]
            self.endResetModel()
        except Exception as e:
            logger.error(f"Ошибка обновления модели оборудования: {str(e)}")
            raise
        finally:
            self._is_resetting = False

    def set_filter(self, search_text: str, column: str = None):
        if self._is_resetting:
            return
        try:
            self._is_resetting = True
            self.beginResetModel()
            search_text = search_text.lower().strip()
            
            def match_word_start(text: str) -> bool:
                return any(word.startswith(search_text) for word in text.lower().split())

            if not search_text:
                self.equipments = self.all_equipments[:]
            else:
                if column is None or column == "Все колонки":
                    self.equipments = [
                        eq for eq in self.all_equipments
                        if any(
                            match_word_start(str(getattr(eq, field) or ""))
                            for field in self.DISPLAY_NAMES.keys()
                        )
                    ]
                else:
                    field = self.COLUMN_MAPPING.get(column)
                    if field:
                        self.equipments = [
                            eq for eq in self.all_equipments
                            if match_word_start(str(getattr(eq, field) or ""))
                        ]
                    else:
                        self.equipments = self.all_equipments[:]

            self.endResetModel()
            logger.debug(f"После фильтрации: {len(self.equipments)} записей")
        except Exception as e:
            logger.error(f"Ошибка применения фильтра: {str(e)}")
            raise
        finally:
            self._is_resetting = False

    def get_equipment(self, row):
        if 0 <= row < len(self.equipments):
            return self.equipments[row]
        return None