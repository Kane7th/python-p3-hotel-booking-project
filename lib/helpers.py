from lib.db.models import session
from lib.db.models.hotel import Hotel
from lib.db.models.room import Room
from lib.db.models.guest import Guest
from lib.db.models.guest_room import GuestRoom
from sqlalchemy.exc import NoResultFound

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

def exit_cli():
    print("Goodbye!")
    exit()
