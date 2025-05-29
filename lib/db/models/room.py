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

    hotel = relationship(
        "Hotel", 
        back_populates="rooms",
        )

    guest_rooms = relationship(
        "GuestRoom",
        back_populates="room",
        cascade="all, delete-orphan",
        overlaps="guests"
    )

    guests = relationship(
        "Guest",
        secondary="guest_rooms",
        back_populates="rooms",
        overlaps="guest_rooms,room"
    )

    @classmethod
    def create(cls, session, hotel_id, room_number, room_type=None, price=None):
        room = cls(
            hotel_id=hotel_id,
            room_number=room_number,
            room_type=room_type,
            price=price,
            is_available=True
        )
        session.add(room)
        session.commit()
        return room

    @classmethod
    def find_by_id(cls, session, room_id):
        return session.query(cls).filter_by(id=room_id).one_or_none()
    
    @classmethod
    def find_by_number_or_id(cls, session, identifier):
        try:
            room_id = int(identifier)
            room = session.query(cls).filter_by(id=room_id).one_or_none()
            if room:
                return [room]
        except ValueError:
            # fallback search by room_number (or partial)
            return session.query(cls).filter(cls.room_number.ilike(f"%{identifier}%")).all()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def delete(self, session):
        session.delete(self)
        session.commit()
