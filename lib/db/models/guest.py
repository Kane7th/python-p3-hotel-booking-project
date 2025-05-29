from sqlalchemy import Column, Integer, String, DateTime, or_
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

    guest_rooms = relationship(
        "GuestRoom",
        back_populates="guest",
        cascade="all, delete-orphan",
        overlaps="rooms",
    )

    rooms = relationship(
        "Room",
        secondary="guest_rooms",
        back_populates="guests",
        overlaps="guest_rooms,guest"
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create(cls, session, first_name, last_name, email, phone=None):
        guest = cls(first_name=first_name, last_name=last_name, email=email, phone=phone)
        session.add(guest)
        session.commit()
        return guest

    @classmethod
    def find_by_id(cls, session, guest_id):
        return session.query(cls).filter_by(id=guest_id).one_or_none()
    
    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter(
        (cls.first_name.ilike(f"%{name}%")) | (cls.last_name.ilike(f"%{name}%"))
        ).all()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def delete(self, session):
        session.delete(self)
        session.commit()
