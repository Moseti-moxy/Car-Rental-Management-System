import uuid
from models.customer import Customer
from models.car import Car
from models.rental import Rental
from utils.storage import (load_customers, save_customers, load_cars, save_cars,
                            load_rentals, save_rentals, find_customer, find_car, find_rental)
from utils.display import (display_customers, display_cars, display_rentals,
                            print_success, print_error, print_info)

def cmd_add_customer(args):
    customers = load_customers()
    if find_customer(args.email, customers):
        print_error(f"Customer '{args.email}' already exists.")
        return
    customers.append(Customer(args.name, args.email, args.phone))
    save_customers(customers)
    print_success(f"Customer '{args.name}' registered successfully.")

def cmd_list_customers(args):
    display_customers(load_customers())

def cmd_search_customer(args):
    customers = load_customers()
    results = [c for c in customers if args.query.lower() in c.name.lower() or args.query.lower() in c.email.lower()]
    if not results:
        print_info(f"No customers found matching '{args.query}'.")
        return
    display_customers(results)

def cmd_delete_customer(args):
    customers = load_customers()
    customer = find_customer(args.email, customers)
    if not customer:
        print_error(f"Customer '{args.email}' not found.")
        return
    customers.remove(customer)
    save_customers(customers)
    print_success(f"Customer '{args.email}' removed.")

def cmd_add_car(args):
    cars = load_cars()
    if find_car(args.plate, cars):
        print_error(f"Car '{args.plate}' already exists.")
        return
    cars.append(Car(args.plate, args.make, args.model, args.year, args.category, args.rate))
    save_cars(cars)
    print_success(f"Car '{args.year} {args.make} {args.model}' added successfully.")

def cmd_list_cars(args):
    display_cars(load_cars(), available_only=False)

def cmd_available_cars(args):
    display_cars(load_cars(), available_only=True)

def cmd_delete_car(args):
    cars = load_cars()
    car = find_car(args.plate, cars)
    if not car:
        print_error(f"Car '{args.plate}' not found.")
        return
    if not car.is_available():
        print_error(f"Car '{args.plate}' is currently rented.")
        return
    cars.remove(car)
    save_cars(cars)
    print_success(f"Car '{args.plate}' removed.")

def cmd_rent_car(args):
    customers = load_customers()
    cars = load_cars()
    rentals = load_rentals()
    customer = find_customer(args.email, customers)
    if not customer:
        print_error(f"Customer '{args.email}' not found. Register them first.")
        return
    car = find_car(args.plate, cars)
    if not car:
        print_error(f"Car '{args.plate}' not found.")
        return
    if not car.is_available():
        print_error(f"Car '{args.plate}' is currently rented out.")
        return
    rental_id = str(uuid.uuid4())[:8].upper()
    rental = Rental(rental_id, args.email, args.plate, args.start_date, args.return_date)
    car.mark_rented()
    customer.add_rental(rental_id)
    rentals.append(rental)
    save_rentals(rentals)
    save_cars(cars)
    save_customers(customers)
    print_success(f"Car '{args.plate}' rented to '{args.email}'. Rental ID: {rental_id}")

def cmd_return_car(args):
    rentals = load_rentals()
    cars = load_cars()
    rental = find_rental(args.rental_id, rentals)
    if not rental:
        print_error(f"Rental ID '{args.rental_id}' not found.")
        return
    if rental.status == "returned":
        print_error(f"Rental '{args.rental_id}' already returned.")
        return
    car = find_car(rental.car_plate, cars)
    if not car:
        print_error(f"Car '{rental.car_plate}' not found.")
        return
    rental.process_return(car.rate_per_day, args.return_date)
    car.mark_available()
    save_rentals(rentals)
    save_cars(cars)
    print_success(f"Car '{rental.car_plate}' returned. Total cost: ${rental.total_cost:,.2f}")

def cmd_list_rentals(args):
    display_rentals(load_rentals())

def cmd_view_rental(args):
    rentals = load_rentals()
    rental = find_rental(args.rental_id, rentals)
    if not rental:
        print_error(f"Rental ID '{args.rental_id}' not found.")
        return
    display_rentals([rental])
