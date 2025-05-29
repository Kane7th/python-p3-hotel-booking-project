#!/usr/bin/env python3
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click
from lib.db.models import session
from lib.helpers import (
    list_hotels, view_hotel_details,
    list_all_guests_with_bookings, view_guest_bookings,
    book_room, cancel_booking,
    create_guest, delete_guest,
    find_guest, find_hotel, find_room,
    list_rooms_with_status
)

def select_from_list(items, item_name):
    """Helper to select one item from a list if multiple found."""
    if not items:
        click.echo(f"No {item_name} found.")
        return None
    if len(items) == 1:
        return items[0]

    click.echo(f"Multiple {item_name}s found:")
    for idx, item in enumerate(items, start=1):
        if item_name == "guest":
            click.echo(f"{idx}. [{item.id}] {item.first_name} {item.last_name}")
        elif item_name == "hotel":
            click.echo(f"{idx}. [{item.id}] {item.name} - {item.city}, {item.country}")
        elif item_name == "room":
            click.echo(f"{idx}. [{item.id}] Room {item.room_number} ({item.room_type})")
        else:
            click.echo(f"{idx}. {item}")

    choice = click.prompt(f"Select {item_name} by number", type=int)
    if 1 <= choice <= len(items):
        return items[choice - 1]
    else:
        click.echo("Invalid selection.")
        return None

@click.command()
def cli():
    """Hotel Booking CLI - Browse, manage, and book hotel stays."""
    click.echo("🏨 Welcome to the Hotel Booking CLI!")

    while True:
        click.echo("\n📋 Main Menu:")
        click.echo("1. List all hotels")
        click.echo("2. View hotel details")
        click.echo("3. List all guests")
        click.echo("4. View guest bookings")
        click.echo("5. Create a new guest")
        click.echo("6. Delete a guest")
        click.echo("7. Create a new booking")
        click.echo("8. Cancel a booking")
        click.echo("9. List all rooms in a hotel with booking status")
        click.echo("10. Exit")

        choice = click.prompt("Enter your choice (1-10)", type=int)

        if choice == 1:
            list_hotels()

        elif choice == 2:
            identifier = click.prompt("Enter hotel name or ID")
            hotels = find_hotel(session, identifier)
            hotel = select_from_list(hotels, "hotel")
            if hotel:
                view_hotel_details(hotel.id)

        elif choice == 3:
            list_all_guests_with_bookings(session)

        elif choice == 4:
            identifier = click.prompt("Enter guest name or ID")
            guests = find_guest(session, identifier)
            guest = select_from_list(guests, "guest")
            if guest:
                view_guest_bookings(guest.id)

        elif choice == 5:
            create_guest(session)

        elif choice == 6:
            identifier = click.prompt("Enter guest name or ID to delete")
            guests = find_guest(session, identifier)
            guest = select_from_list(guests, "guest")
            if guest:
                guest.delete(session)
                click.echo("Guest deleted successfully!")

        elif choice == 7:
            guest_identifier = click.prompt("Enter guest name or ID")
            guests = find_guest(session, guest_identifier)
            guest = select_from_list(guests, "guest")
            if not guest:
                continue

            room_identifier = click.prompt("Enter room number or ID")
            rooms = find_room(session, room_identifier)
            room = select_from_list(rooms, "room")
            if not room:
                continue

            if not room.is_available:
                click.echo("Sorry, this room is already booked.")
                continue

            # Prompt booking date
            date_str = click.prompt("Enter booking date (YYYY-MM-DD HH:MM), leave blank for now", default="")
            if date_str.strip():
                try:
                    booking_date = datetime.strptime(date_str.strip(), "%Y-%m-%d %H:%M")
                except ValueError:
                    click.echo("Invalid date format. Using current date/time instead.")
                    booking_date = None
            else:
                booking_date = None

            try:
                from lib.db.models.guest_room import GuestRoom
                booking = GuestRoom(guest_id=guest.id, room_id=room.id)
                if booking_date:
                    booking.booking_date = booking_date
                room.is_available = False
                session.add(booking)
                session.commit()
                click.echo("Room booked successfully.")
            except Exception as e:
                session.rollback()
                click.echo(f"Booking failed: {e}")

        elif choice == 8:
            guest_identifier = click.prompt("Enter guest name or ID")
            guests = find_guest(session, guest_identifier)
            guest = select_from_list(guests, "guest")
            if not guest:
                continue

            room_identifier = click.prompt("Enter room number or ID")
            rooms = find_room(session, room_identifier)
            room = select_from_list(rooms, "room")
            if not room:
                continue

            try:
                booking = session.query(GuestRoom).filter_by(guest_id=guest.id, room_id=room.id).one()
                session.delete(booking)
                room.is_available = True
                session.commit()
                click.echo("Booking cancelled successfully.")
            except Exception as e:
                session.rollback()
                click.echo(f"Cancellation failed: {e}")

        elif choice == 9:
            identifier = click.prompt("Enter hotel name or ID")
            hotels = find_hotel(session, identifier)
            hotel = select_from_list(hotels, "hotel")
            if hotel:
                list_rooms_with_status(session, hotel)

        elif choice == 10:
            click.echo("👋 Goodbye!")
            break

        else:
            click.echo("❌ Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    cli()
