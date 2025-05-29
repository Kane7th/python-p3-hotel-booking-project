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

    @classmethod
    def create(cls, session, name, address=None, city=None, country=None):
        hotel = cls(name=name, address=address, city=city, country=country)
        session.add(hotel)
        session.commit()
        return hotel

    @classmethod
    def find_by_id(cls, session, hotel_id):
        return session.query(cls).filter_by(id=hotel_id).one_or_none()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def delete(self, session):
        session.delete(self)
        session.commit()
