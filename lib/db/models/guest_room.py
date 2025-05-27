from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class GuestRoom(Base):
    __tablename__ = "guest_rooms"

    guest_id = Column(Integer, ForeignKey("guests.id"), primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), primary_key=True)
    booking_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    guest = relationship(
        "Guest",
        back_populates="guest_rooms",
        overlaps="rooms,guests"
    )
    room = relationship(
        "Room",
        back_populates="guest_rooms",
        overlaps="guests,rooms"
    )

