#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click
from lib.db.models import session
from lib.helpers import (
    list_hotels, view_hotel_details,
    list_guests, view_guest_bookings,
    book_room, cancel_booking,
    create_guest, delete_guest
)

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
        click.echo("9. Exit")

        choice = click.prompt("Enter your choice (1-9)", type=int)

        if choice == 1:
            list_hotels()
        elif choice == 2:
            hotel_id = click.prompt("Enter hotel ID", type=int)
            view_hotel_details(hotel_id)
        elif choice == 3:
            list_guests()
        elif choice == 4:
            guest_id = click.prompt("Enter guest ID", type=int)
            view_guest_bookings(guest_id)
        elif choice == 5:
            create_guest(session)
        elif choice == 6:
            delete_guest(session)
        elif choice == 7:
            guest_id = click.prompt("Enter Guest ID", type=int)
            room_id = click.prompt("Enter Room ID to book", type=int)
            book_room(guest_id, room_id)
        elif choice == 8:
            guest_id = click.prompt("Enter Guest ID", type=int)
            room_id = click.prompt("Enter Room ID to cancel booking", type=int)
            cancel_booking(guest_id, room_id)
        elif choice == 9:
            click.echo("👋 Goodbye!")
            break
        else:
            click.echo("❌ Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    cli()
