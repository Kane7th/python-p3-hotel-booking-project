import click
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from lib.db.models import session
from lib.db.models.hotel import Hotel
from lib.db.models.room import Room
from lib.db.models.guest import Guest
from lib.db.models.guest_room import GuestRoom

def list_hotels():
    hotels = session.query(Hotel).all()
    if not hotels:
        print("No hotels found.")
        return
    print("\n--- Hotels ---")
    for hotel in hotels:
        print(f"[{hotel.id}] {hotel.name} - {hotel.city}, {hotel.country}")

def view_hotel_details(hotel_id):
    try:
        hotel = session.query(Hotel).filter_by(id=hotel_id).one()
        print(f"\nHotel: {hotel.name}")
        print(f"Address: {hotel.address}")
        print(f"City: {hotel.city}")
        print(f"Country: {hotel.country}")
        print("\nRooms:")
        for room in hotel.rooms:
            print(f" - Room {room.room_number} ({room.room_type}) - ${room.price} - {'Available' if room.is_available else 'Booked'}")
    except NoResultFound:
        print("Hotel not found.")

def list_guests():
    guests = session.query(Guest).all()
    if not guests:
        print("No guests found.")
        return
    print("\n--- Guests ---")
    for guest in guests:
        print(f"[{guest.id}] {guest.first_name} {guest.last_name} - {guest.email}")

def view_guest_bookings(guest_id):
    try:
        guest = session.query(Guest).filter_by(id=guest_id).one()
        bookings = guest.guest_rooms

        if not bookings:
            print(f"No bookings found for guest {guest.first_name} {guest.last_name}.")
            return

        print(f"\nBookings for {guest.first_name} {guest.last_name}:")
        for booking in bookings:
            room = booking.room
            hotel = room.hotel
            print(f" - Hotel: {hotel.name}, Room: {room.room_number} ({room.room_type}), Booked on: {booking.booking_date.strftime('%Y-%m-%d %H:%M:%S')}")
    except NoResultFound:
        print("Guest not found.")
    except Exception as e:
        print(f"Failed to retrieve bookings: {e}")

def book_room(guest_id, room_id):
    try:
        room = session.query(Room).filter_by(id=room_id).one()

        if not room.is_available:
            print("Sorry, this room is already booked.")
            return

        booking = GuestRoom(guest_id=guest_id, room_id=room_id)
        room.is_available = False

        session.add(booking)
        session.commit()
        print("Room booked successfully.")
    except NoResultFound:
        print("Room or Guest not found.")
    except Exception as e:
        session.rollback()
        print(f"Booking failed: {e}")

def cancel_booking(guest_id, room_id):
    try:
        booking = session.query(GuestRoom).filter_by(guest_id=guest_id, room_id=room_id).one()
        session.delete(booking)

        room = session.query(Room).filter_by(id=room_id).one()
        room.is_available = True

        session.commit()
        print("Booking cancelled successfully.")
    except NoResultFound:
        print("Booking not found.")
    except Exception as e:
        session.rollback()
        print(f"Cancellation failed: {e}")

def create_guest(session: Session):
    first = click.prompt("Enter first name")
    last = click.prompt("Enter last name")
    email = click.prompt("Enter email")
    phone = click.prompt("Enter phone", default="")
    try:
        Guest.create(session, first, last, email, phone)
        click.echo("Guest created successfully!")
    except Exception as e:
        click.echo(f"Error creating guest: {e}")

def delete_guest(session: Session):
    guest_id = click.prompt("Enter Guest ID to delete", type=int)
    guest = Guest.find_by_id(session, guest_id)
    if guest:
        guest.delete(session)
        click.echo("Guest deleted successfully!")
    else:
        click.echo("Guest not found.")

def find_guest(session, identifier):
    try:
        guest_id = int(identifier)
        guest = Guest.find_by_id(session, guest_id)
        if guest:
            return [guest]
    except ValueError:
        pass
    return Guest.find_by_name(session, identifier)

def find_hotel(session, identifier):
    try:
        hotel_id = int(identifier)
        hotel = Hotel.find_by_id(session, hotel_id)
        if hotel:
            return [hotel]
    except ValueError:
        pass
    return Hotel.find_by_name(session, identifier)

def find_room(session, identifier):
    try:
        room_id = int(identifier)
        room = Room.find_by_id(session, room_id)
        if room:
            return [room]
    except ValueError:
        pass
    # fallback by room_number substring match
    return session.query(Room).filter(Room.room_number.ilike(f"%{identifier}%")).all()

def list_rooms_with_status(session, hotel):
    print(f"\nRooms in hotel '{hotel.name}':")
    for room in hotel.rooms:
        booked = len(room.guest_rooms) > 0
        status = "Booked" if booked else "Vacant"
        print(f"Room {room.room_number} ({room.room_type}) - {status}")

def list_all_guests_with_bookings(session):
    guests = session.query(Guest).all()
    for guest in guests:
        print(f"Guest: {guest.first_name} {guest.last_name} (ID: {guest.id})")
        if guest.guest_rooms:
            for booking in guest.guest_rooms:
                room = booking.room
                hotel = room.hotel
                date = booking.booking_date.strftime("%Y-%m-%d")
                print(f"  Booked Room {room.room_number} at {hotel.name} on {date}")
        else:
            print("  No bookings")

def exit_cli():
    print("Goodbye!")
    exit()
