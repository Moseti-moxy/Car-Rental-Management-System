# 🚗 Car Rental Management System

A command-line application for managing customers, vehicles, and rental transactions.

## Setup
```bash
pip install -r requirements.txt
```

## Commands

### Customers
```bash
python main.py add-customer --name "Jane Doe" --email "jane@email.com" --phone "0712345678"
python main.py list-customers
python main.py search-customer --query "Jane"
python main.py delete-customer --email "jane@email.com"
```

### Cars
```bash
python main.py add-car --plate "KCA123A" --make "Toyota" --model "Camry" --year 2022 --category Sedan --rate 50
python main.py list-cars
python main.py available-cars
python main.py delete-car --plate "KCA123A"
```

### Rentals
```bash
python main.py rent-car --email "jane@email.com" --plate "KCA123A" --start-date 2025-06-01
python main.py return-car --rental-id "ABC12345" --return-date 2025-06-05
python main.py list-rentals
python main.py view-rental --rental-id "ABC12345"
```

## Run Tests
```bash
pytest tests/ -v
```

## Data Model
- **Customer → Rentals** (one-to-many)
- **Car → Rentals** (one-to-many)
- **Rental** links Customer ↔ Car (many-to-many relationship)
