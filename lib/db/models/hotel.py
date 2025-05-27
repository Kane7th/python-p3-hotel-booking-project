from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    city = Column(String(100))
    country = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    rooms = relationship("Room", back_populates="hotel", cascade="all, delete-orphan")
