import argparse
import sys
from cli.commands import (cmd_add_customer, cmd_list_customers, cmd_search_customer, cmd_delete_customer,
                           cmd_add_car, cmd_list_cars, cmd_available_cars, cmd_delete_car,
                           cmd_rent_car, cmd_return_car, cmd_list_rentals, cmd_view_rental)

def build_parser():
    parser = argparse.ArgumentParser(prog="carrental", description="🚗 Car Rental Management System")
    sub = parser.add_subparsers(dest="command", help="Available commands")
    sub.required = True

    p = sub.add_parser("add-customer", help="Register a new customer")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)
    p.add_argument("--phone", default="")
    p.set_defaults(func=cmd_add_customer)

    p = sub.add_parser("list-customers", help="List all customers")
    p.set_defaults(func=cmd_list_customers)

    p = sub.add_parser("search-customer", help="Search customers")
    p.add_argument("--query", required=True)
    p.set_defaults(func=cmd_search_customer)

    p = sub.add_parser("delete-customer", help="Remove a customer")
    p.add_argument("--email", required=True)
    p.set_defaults(func=cmd_delete_customer)

    p = sub.add_parser("add-car", help="Add a vehicle")
    p.add_argument("--plate", required=True)
    p.add_argument("--make", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--year", required=True, type=int)
    p.add_argument("--category", default="Sedan", choices=["Sedan","SUV","Truck","Van","Convertible","Hatchback","Other"])
    p.add_argument("--rate", dest="rate", type=float, default=0.0)
    p.set_defaults(func=cmd_add_car)

    p = sub.add_parser("list-cars", help="List all vehicles")
    p.set_defaults(func=cmd_list_cars)

    p = sub.add_parser("available-cars", help="List available vehicles")
    p.set_defaults(func=cmd_available_cars)

    p = sub.add_parser("delete-car", help="Remove a vehicle")
    p.add_argument("--plate", required=True)
    p.set_defaults(func=cmd_delete_car)

    p = sub.add_parser("rent-car", help="Rent a car to a customer")
    p.add_argument("--email", required=True)
    p.add_argument("--plate", required=True)
    p.add_argument("--start-date", dest="start_date", default="")
    p.add_argument("--return-date", dest="return_date", default="")
    p.set_defaults(func=cmd_rent_car)

    p = sub.add_parser("return-car", help="Process a vehicle return")
    p.add_argument("--rental-id", dest="rental_id", required=True)
    p.add_argument("--return-date", dest="return_date", default="")
    p.set_defaults(func=cmd_return_car)

    p = sub.add_parser("list-rentals", help="View all rental records")
    p.set_defaults(func=cmd_list_rentals)

    p = sub.add_parser("view-rental", help="View a specific rental")
    p.add_argument("--rental-id", dest="rental_id", required=True)
    p.set_defaults(func=cmd_view_rental)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting Car Rental System.")
        sys.exit(0)

if __name__ == "__main__":
    main()
