# Hotel Booking System

A Python-based hotel booking system using SQLAlchemy, Alembic, and Faker. This project models hotel entities such as customers, rooms, and bookings. It also supports testing, mock data generation, and database migrations.

---

# 📋 Overview of Key Files and Functions

CLI Script (cli.py)
This is the main entry point of the application. It uses the click library to provide a user-friendly, interactive command-line interface for browsing hotels, viewing details, managing guests, and handling bookings.

Main Menu: Displays options like listing hotels, viewing hotel details, listing guests, viewing guest bookings, creating bookings, canceling bookings, and exiting the application.

User Input Handling: Prompts the user for inputs such as hotel ID, guest ID, and room ID and validates these inputs.

Function Calls: Calls helper functions defined in helpers.py to perform database operations and display results.

Helpers (helpers.py)
This module contains functions that interact directly with the database via SQLAlchemy sessions. These functions handle the core logic and CRUD operations:

list_hotels(): Fetches and lists all hotels with basic information.

view_hotel_details(hotel_id): Shows detailed information for a specific hotel including its rooms and their availability.

list_guests(): Lists all guests with their contact info.

view_guest_bookings(guest_id): Displays all room bookings for a given guest.

book_room(guest_id, room_id): Creates a booking for a guest in a specific room, checking room availability.

cancel_booking(guest_id, room_id): Cancels an existing booking and marks the room as available.

exit_cli(): Gracefully exits the CLI application.

Each helper function manages exceptions and database commits or rollbacks to ensure robust operation.

Models (models/)
Defines the ORM classes using SQLAlchemy, modeling the database schema with relationships and constraints:

Hotel (hotel.py): Represents a hotel entity with attributes like name, address, city, country, and a one-to-many relationship with rooms.

Room (room.py): Models hotel rooms with details such as room number, type, price, availability, and references to its hotel. Also has many-to-many relationships with guests through bookings.

Guest (guest.py): Represents guests with personal details and many-to-many relationships with rooms through bookings.

GuestRoom (guest_room.py): Join table modeling bookings between guests and rooms. Includes booking date and timestamps.

Each model uses SQLAlchemy relationships with appropriate cascading and back_populates to maintain referential integrity.

Database Migrations (Alembic)
Although not edited frequently, Alembic is used to manage schema changes through version-controlled migrations. It ensures the database structure evolves consistently with the codebase.

Seed Script (seed.py)
Populates the database with realistic mock data using the Faker library, useful for testing and development purposes.

---

# 🛠 How to Use This Project

Run the CLI by executing python cli.py (ensure virtual environment and dependencies are installed).

Use the interactive menu to:

Browse hotels and rooms

View guest information and bookings

Create and cancel bookings

Extend or modify helper functions or models to fit additional business logic or features.

---

## 🚀 Features

- Object-oriented design
- Room and customer management
- Booking management with validation
- Auto-generated fake data (Faker)
- Database schema migrations (Alembic)
- Debugging (ipdb)
- Pretty console tables (tabulate)
- Unit testing with Pytest
- Mocks and testing utilities (pytest-mock)

---

## 🛠 Tech Stack

- Python 3.12
- SQLAlchemy
- Alembic
- Faker
- Tabulate
- IPython / ipdb
- Pytest + pytest-mock

---

## 📦 Installation

### 1. Clone the repository:
```bash
git clone git@github.com:Kane7th/python-p3-hotel-booking-project.git
cd hotel-booking-system
2. Install dependencies with Pipenv:
bash
Copy
Edit
pipenv install
3. Activate the virtual environment:
bash
Copy
Edit
pipenv shell
4. Setup the database:
bash
Copy
Edit
alembic upgrade head

5. (Optional) Seed the database with fake data:
bash
Copy
Edit
python seed.py
✅ Running Tests
bash
Copy
Edit
pytest

📁 Project Structure
markdown
Copy
Edit
.
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── room.py
│   ├── booking.py
├── seed.py
├── alembic/
├── alembic.ini
├── Pipfile
├── Pipfile.lock
├── README.md
└── tests/
    ├── test_models.py

📌 Notes
Ensure SQLite is configured.

Alembic is used for version-controlling database schema.

Faker can populate test databases with realistic-looking data.

👤 Author
Kane Kabena
Email: onekaneldn@gmail.com