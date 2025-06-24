import logging
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtGui import QColor
from sqlalchemy.orm import Session

from bd.calibration_event_model import CalibrationEvent


logger = logging.getLogger(__name__)

class CalibrationEventTableModel(QAbstractTableModel):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.events = []
        self.headers = ["Номер", "Дни до поверки", "Цвет подсветки"]
        self.refresh()

    def rowCount(self, parent=QModelIndex()):
        return len(self.events)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        event = self.events[index.row()]
        column = index.column()
        
        if role == Qt.DisplayRole:
            if column == 0:
                return str(index.row() + 1)  
            elif column == 1:
                return str(event.check_days)
            elif column == 2:
                return event.highlight_color
        elif role == Qt.BackgroundRole:
            return QColor(event.highlight_color) 
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
        return None

    def refresh(self):
        try:
            self.beginResetModel()
            self.events = self.session.query(CalibrationEvent).order_by(CalibrationEvent.id).all()
            self.endResetModel()
        except Exception as e:
            logger.error(f"Ошибка обновления модели событий: {str(e)}")
            raise

    def get_event(self, row):
        if 0 <= row < len(self.events):
            return self.events[row]
        return None