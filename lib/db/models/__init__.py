from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .hotel import Hotel
from .room import Room
from .guest import Guest
from .guest_room import GuestRoom
