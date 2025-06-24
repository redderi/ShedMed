from sqlalchemy import Column, Integer, String

from bd.equipment_model import Base


class CalibrationEvent(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    check_days = Column(Integer, nullable=False) 
    highlight_color = Column(String, nullable=False) 