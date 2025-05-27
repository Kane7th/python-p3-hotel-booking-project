from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)

    rooms = relationship(
        "Room",
        secondary="guest_rooms",
        back_populates="guests",
        overlaps="guest_rooms,guests"
    )

    guest_rooms = relationship(
        "GuestRoom", 
        back_populates="guest", 
        overlaps="rooms,guests"
    )
