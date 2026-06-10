import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CUSTOMERS_FILE = os.path.join(DATA_DIR, "customers.json")
CARS_FILE = os.path.join(DATA_DIR, "cars.json")
RENTALS_FILE = os.path.join(DATA_DIR, "rentals.json")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def save_json(filepath: str, data: list):
    ensure_data_dir()
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"[ERROR] Could not save data: {e}")

def load_json(filepath: str) -> list:
    ensure_data_dir()
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"[ERROR] Could not load data: {e}")
        return []

def save_customers(customers: list):
    save_json(CUSTOMERS_FILE, [c.to_dict() for c in customers])

def load_customers() -> list:
    from models.customer import Customer
    return [Customer.from_dict(d) for d in load_json(CUSTOMERS_FILE)]

def save_cars(cars: list):
    save_json(CARS_FILE, [c.to_dict() for c in cars])

def load_cars() -> list:
    from models.car import Car
    return [Car.from_dict(d) for d in load_json(CARS_FILE)]

def save_rentals(rentals: list):
    save_json(RENTALS_FILE, [r.to_dict() for r in rentals])

def load_rentals() -> list:
    from models.rental import Rental
    return [Rental.from_dict(d) for d in load_json(RENTALS_FILE)]

def find_customer(email: str, customers: list):
    for c in customers:
        if c.email.lower() == email.lower():
            return c
    return None

def find_car(plate: str, cars: list):
    for c in cars:
        if c.plate.upper() == plate.upper():
            return c
    return None

def find_rental(rental_id: str, rentals: list):
    for r in rentals:
        if r.rental_id == rental_id:
            return r
    return None
