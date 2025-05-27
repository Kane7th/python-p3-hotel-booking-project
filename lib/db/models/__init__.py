from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///hotel_booking.db', echo=True)  # or your actual DB URL

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

from .hotel import Hotel
from .room import Room
from .guest import Guest
from .guest_room import GuestRoom
