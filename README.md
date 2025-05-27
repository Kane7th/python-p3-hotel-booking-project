# Hotel Booking System

A Python-based hotel booking system using SQLAlchemy, Alembic, and Faker. This project models hotel entities such as customers, rooms, and bookings. It also supports testing, mock data generation, and database migrations.

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

- Python 3.8
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
git clone https://github.com/your-username/hotel-booking-system.git
cd hotel-booking-system
```

### 2. Install dependencies with Pipenv:
```bash
pipenv install
```

### 3. Activate the virtual environment:
```bash
pipenv shell
```

### 4. Setup the database:
```bash
alembic upgrade head
```

### 5. (Optional) Seed the database with fake data:
```bash
python seed.py
```

---

## ✅ Running Tests
```bash
pytest
```

---

## 📁 Project Structure
```
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
```

---

## 📌 Notes
- Ensure PostgreSQL or SQLite is configured if applicable.
- Alembic is used for version-controlling database schema.
- Faker can populate test databases with realistic-looking data.

---

## 👤 Author
**Kane Kabena**  
Email: onekaneldn@gmail.com