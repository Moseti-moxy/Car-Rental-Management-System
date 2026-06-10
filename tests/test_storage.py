import pytest
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models.customer import Customer
from models.car import Car
from models.rental import Rental
from utils.storage import (save_customers, load_customers, save_cars, load_cars,
                            save_rentals, load_rentals, find_customer, find_car,
                            find_rental, CUSTOMERS_FILE, CARS_FILE, RENTALS_FILE)

@pytest.fixture(autouse=True)
def clean_files():
    for f in [CUSTOMERS_FILE, CARS_FILE, RENTALS_FILE]:
        if os.path.exists(f):
            os.remove(f)
    yield
    for f in [CUSTOMERS_FILE, CARS_FILE, RENTALS_FILE]:
        if os.path.exists(f):
            os.remove(f)

class TestStorage:
    def test_save_load_customers(self):
        customers = [Customer("Jane", "jane@email.com"), Customer("John", "john@email.com")]
        save_customers(customers)
        loaded = load_customers()
        assert len(loaded) == 2

    def test_save_load_cars(self):
        cars = [Car("KCA123A", "Toyota", "Camry", 2022, "Sedan", 50.0)]
        save_cars(cars)
        loaded = load_cars()
        assert loaded[0].plate == "KCA123A"

    def test_save_load_rentals(self):
        rentals = [Rental("R001", "jane@email.com", "KCA123A", "2025-06-01")]
        save_rentals(rentals)
        loaded = load_rentals()
        assert loaded[0].rental_id == "R001"

    def test_find_customer(self):
        customers = [Customer("Jane", "jane@email.com")]
        assert find_customer("jane@email.com", customers) is not None

    def test_find_customer_case_insensitive(self):
        customers = [Customer("Jane", "jane@email.com")]
        assert find_customer("JANE@EMAIL.COM", customers) is not None

    def test_find_customer_not_found(self):
        assert find_customer("nobody@email.com", []) is None

    def test_find_car(self):
        cars = [Car("KCA123A", "Toyota", "Camry", 2022)]
        assert find_car("kca123a", cars) is not None

    def test_find_car_not_found(self):
        assert find_car("ZZZ999Z", []) is None

    def test_find_rental(self):
        rentals = [Rental("R001", "jane@email.com", "KCA123A")]
        assert find_rental("R001", rentals) is not None

    def test_load_empty_returns_list(self):
        assert load_customers() == []
        assert load_cars() == []
        assert load_rentals() == []
