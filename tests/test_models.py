import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models.customer import Customer
from models.car import Car
from models.rental import Rental

class TestCustomer:
    def test_create_customer(self):
        c = Customer("Jane Doe", "jane@email.com", "0712345678")
        assert c.name == "Jane Doe"
        assert c.rental_history == []

    def test_empty_name_raises(self):
        with pytest.raises(ValueError):
            Customer("", "jane@email.com")

    def test_empty_email_raises(self):
        with pytest.raises(ValueError):
            Customer("Jane", "")

    def test_add_rental(self):
        c = Customer("Jane", "jane@email.com")
        c.add_rental("ABC123")
        assert "ABC123" in c.rental_history

    def test_no_duplicate_rentals(self):
        c = Customer("Jane", "jane@email.com")
        c.add_rental("ABC123")
        c.add_rental("ABC123")
        assert c.rental_history.count("ABC123") == 1

    def test_to_dict_from_dict(self):
        c = Customer("Jane", "jane@email.com", "0712345678")
        c.add_rental("ABC123")
        restored = Customer.from_dict(c.to_dict())
        assert restored.name == "Jane"
        assert "ABC123" in restored.rental_history

class TestCar:
    def test_create_car(self):
        car = Car("KCA123A", "Toyota", "Camry", 2022, "Sedan", 50.0)
        assert car.plate == "KCA123A"
        assert car.status == "available"

    def test_plate_uppercased(self):
        car = Car("kca123a", "Toyota", "Camry", 2022)
        assert car.plate == "KCA123A"

    def test_empty_plate_raises(self):
        with pytest.raises(ValueError):
            Car("", "Toyota", "Camry", 2022)

    def test_empty_make_raises(self):
        with pytest.raises(ValueError):
            Car("KCA123A", "", "Camry", 2022)

    def test_invalid_category_defaults(self):
        car = Car("KCA123A", "Toyota", "Camry", 2022, "InvalidCat")
        assert car.category == "Other"

    def test_mark_rented(self):
        car = Car("KCA123A", "Toyota", "Camry", 2022)
        car.mark_rented()
        assert not car.is_available()

    def test_mark_available(self):
        car = Car("KCA123A", "Toyota", "Camry", 2022)
        car.mark_rented()
        car.mark_available()
        assert car.is_available()

    def test_to_dict_from_dict(self):
        car = Car("KCA123A", "Toyota", "Camry", 2022, "Sedan", 50.0)
        car.mark_rented()
        restored = Car.from_dict(car.to_dict())
        assert restored.status == "rented"

class TestRental:
    def test_create_rental(self):
        r = Rental("R001", "jane@email.com", "KCA123A", "2025-06-01")
        assert r.status == "active"

    def test_empty_id_raises(self):
        with pytest.raises(ValueError):
            Rental("", "jane@email.com", "KCA123A")

    def test_empty_email_raises(self):
        with pytest.raises(ValueError):
            Rental("R001", "", "KCA123A")

    def test_empty_plate_raises(self):
        with pytest.raises(ValueError):
            Rental("R001", "jane@email.com", "")

    def test_process_return(self):
        r = Rental("R001", "jane@email.com", "KCA123A", "2025-06-01")
        r.process_return(50.0, "2025-06-05")
        assert r.status == "returned"
        assert r.total_cost == 200.0

    def test_minimum_one_day_charge(self):
        r = Rental("R001", "jane@email.com", "KCA123A", "2025-06-01")
        r.process_return(50.0, "2025-06-01")
        assert r.total_cost == 50.0

    def test_to_dict_from_dict(self):
        r = Rental("R001", "jane@email.com", "KCA123A", "2025-06-01")
        r.process_return(50.0, "2025-06-05")
        restored = Rental.from_dict(r.to_dict())
        assert restored.total_cost == 200.0
