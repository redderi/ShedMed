import logging
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime, timedelta


logger = logging.getLogger(__name__)
Base = declarative_base()

class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, nullable=False)
    equipment_name = Column(String, nullable=False)
    equipment_type = Column(String)
    serial_number = Column(String)
    location = Column(String)
    calibration_interval = Column(Integer)
    last_calibration_date = Column(DateTime)
    next_calibration_date = Column(DateTime)
    certificate_number = Column(String)
    days_to_calibration = Column(Integer)
    notes = Column(String)

    def update_calibration(self):        
        if isinstance(self.last_calibration_date, date) and not isinstance(self.last_calibration_date, datetime):
            self.last_calibration_date = datetime.combine(self.last_calibration_date, datetime.min.time())
        if (
                self.last_calibration_date
                and isinstance(self.last_calibration_date, datetime)
                and self.calibration_interval is not None
                and self.calibration_interval > 0
            ):
            try:
                self.next_calibration_date = self.last_calibration_date + timedelta(days=self.calibration_interval)
                current_date = datetime.now()
                days_to_calibration = (self.next_calibration_date - current_date).days
                self.days_to_calibration = max(days_to_calibration, 0)
            except Exception as e:
                logger.error(f"Ошибка вычисления калибровки: {str(e)}")
                self.next_calibration_date = None
                self.days_to_calibration = None
        else:
            self.next_calibration_date = None
            self.days_to_calibration = None