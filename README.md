# 🏨 Hotel Booking System

A **Python-based hotel booking system** using **SQLAlchemy**, **Alembic**, and **Faker**. This project models hotel entities such as customers, rooms, and bookings. It also supports testing, mock data generation, and database migrations.

---

## 📋 Overview of Key Files and Functions

### 📂 CLI Script (`cli.py`)
- **Main entry point** using the `click` library for a user-friendly CLI.
- **Main Menu**: List hotels, view details, manage guests/bookings, exit.
- **User Input Handling**: Input validation for hotel ID, guest ID, and room ID.
- **Function Calls**: Delegates tasks to `helpers.py` functions.

---

### 🛠 Helpers (`helpers.py`)
- Interacts directly with the database using SQLAlchemy sessions.
- Contains core logic and CRUD operations:

| Function | Description |
|---------|-------------|
| `list_hotels()` | Lists all hotels with basic info |
| `view_hotel_details(hotel_id)` | Detailed info including room availability |
| `list_guests()` | Lists all guests and contact info |
| `view_guest_bookings(guest_id)` | Guest-specific room bookings |
| `book_room(guest_id, room_id)` | Books a room with availability check |
| `cancel_booking(guest_id, room_id)` | Cancels a booking, updates room status |
| `exit_cli()` | Exits the CLI app |

_All functions manage exceptions and database transactions for robustness._

---

### 🏗 Models (`models/`)
Defined using SQLAlchemy ORM with clear relationships:

- **Hotel (`hotel.py`)**: Name, address, city, country + rooms (1-to-many)
- **Room (`room.py`)**: Room number, type, price, availability + hotel reference, many-to-many with guests
- **Guest (`guest.py`)**: Guest details + bookings (many-to-many)
- **GuestRoom (`guest_room.py`)**: Join table, includes booking dates

---

### 🔄 Database Migrations (Alembic)
- Handles version-controlled schema changes.
- Ensures database consistency as the codebase evolves.

---

### 🌱 Seed Script (`seed.py`)
- Populates the database with mock data via the **Faker** library.
- Useful for testing and development.

---

## 💻 How to Use This Project

1. Run the CLI:
   ```bash
   lib/cli.py
   ```

2. Use the interactive menu to:
   - Browse hotels and rooms
   - View guest info/bookings
   - Create and cancel bookings

3. Extend or modify helper functions/models for additional features.

---

## 🚀 Features

- 🧱 Object-oriented design
- 🛏 Room and customer management
- 📅 Booking logic with validation
- 🧪 Fake data for testing (Faker)
- 🔧 Schema migrations (Alembic)
- 🐞 Debugging tools (ipdb)
- 📊 Console table formatting (tabulate)
- ✅ Unit testing (Pytest + pytest-mock)

---

## 🛠 Tech Stack

- Python 3.12
- SQLAlchemy
- Alembic
- Faker
- Tabulate
- IPython / ipdb

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone git@github.com:Kane7th/python-p3-hotel-booking-project.git
cd hotel-booking-system
```

### 2. Install Dependencies with Pipenv
```bash
pipenv install
```

### 3. Activate Virtual Environment
```bash
pipenv shell
```

### 4. Setup the Database
```bash
alembic upgrade head
```

### 5. (Optional) Seed the Database with Fake Data
```bash
seed.py
```

---

## 📁 Project Structure
```
.
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── room.py
│   ├── hotel.py
│   ├── guest_room.py
├── seed.py
├── debug.py
├── cli.py
├── helpers.py
├── alembic/
├── alembic.ini
├── Pipfile
├── Pipfile.lock
├── README.md

```

---

## 📌 Notes

- Ensure **SQLite** is configured correctly.
- **Alembic** manages version-controlled migrations.
- **Faker** is used to populate the database for testing.
- **DB schema** can be viewed here: https://dbdiagram.io/d/hotel-bookings-project-68344b740240c65c443bddb7

---

## 👤 Author

**Kane Kabena**  
📧 Email: onekaneldn@gmail.com
