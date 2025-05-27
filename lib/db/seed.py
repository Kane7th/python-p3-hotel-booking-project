#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Hotel, Room, Guest, GuestRoom
from datetime import datetime, timedelta

# Setup Faker and DB
fake = Faker()

DATABASE_URL = "sqlite:///./hotel_booking.db"  # adjust if needed

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def seed_hotels(n=5):
    hotels = []
    for _ in range(n):
        hotel = Hotel(
            name=fake.company(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            created_at=fake.date_time_between(start_date='-2y', end_date='now')
        )
        session.add(hotel)
        hotels.append(hotel)
    session.commit()
    return hotels

def seed_rooms(hotels, rooms_per_hotel=10):
    rooms = []
    room_types = ['Single', 'Double', 'Suite', 'Deluxe', 'King', 'Queen']
    for hotel in hotels:
        for _ in range(rooms_per_hotel):
            room = Room(
                hotel=hotel,
                room_number=str(fake.random_int(min=100, max=999)),
                room_type=random.choice(room_types),
                price=round(random.uniform(50, 500), 2),
                is_available=fake.boolean(chance_of_getting_true=80),
                created_at=fake.date_time_between(start_date='-2y', end_date='now')
            )
            session.add(room)
            rooms.append(room)
    session.commit()
    return rooms

def seed_guests(n=20):
    guests = []
    for _ in range(n):
        guest = Guest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            created_at=fake.date_time_between(start_date='-2y', end_date='now')
        )
        session.add(guest)
        guests.append(guest)
    session.commit()
    return guests

def seed_guest_rooms(guests, rooms, max_bookings_per_guest=3):
    for guest in guests:
        bookings = random.randint(1, max_bookings_per_guest)
        booked_rooms = random.sample(rooms, bookings)
        for room in booked_rooms:
            booking_date = fake.date_time_between(start_date='-1y', end_date='now')
            guest_room = GuestRoom(
                guest=guest,
                room=room,
                booking_date=booking_date,
                created_at=booking_date
            )
            session.add(guest_room)
    session.commit()

def main():
    print("Seeding hotels...")
    hotels = seed_hotels()
    print(f"Created {len(hotels)} hotels.")

    print("Seeding rooms...")
    rooms = seed_rooms(hotels)
    print(f"Created {len(rooms)} rooms.")

    print("Seeding guests...")
    guests = seed_guests()
    print(f"Created {len(guests)} guests.")

    print("Seeding guest-room bookings...")
    seed_guest_rooms(guests, rooms)
    print("Guest-room bookings created.")

    print("Seeding completed!")

if __name__ == "__main__":
    # Create tables if not exist
    Base.metadata.create_all(engine)
    main()
