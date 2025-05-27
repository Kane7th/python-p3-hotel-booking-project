from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Boolean
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    room_number = Column(String(50), nullable=False)
    room_type = Column(String(50))
    price = Column(Numeric(10, 2))
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    hotel = relationship("Hotel", back_populates="rooms")
    guests = relationship(
        "Guest",
        secondary="guest_rooms",
        back_populates="rooms",
        overlaps="guest_rooms,rooms"
    )
    guest_rooms = relationship(
        "GuestRoom",
        back_populates="room",
        overlaps="guests,rooms"
    )
