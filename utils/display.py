from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def print_success(msg: str):
    console.print(f"[bold green]✔ {msg}[/bold green]")

def print_error(msg: str):
    console.print(f"[bold red]✘ {msg}[/bold red]")

def print_info(msg: str):
    console.print(f"[bold cyan]ℹ {msg}[/bold cyan]")

def display_customers(customers: list):
    if not customers:
        print_info("No customers found.")
        return
    table = Table(title="👥 Registered Customers", box=box.ROUNDED)
    table.add_column("Name", style="bold yellow")
    table.add_column("Email", style="cyan")
    table.add_column("Phone", style="green")
    table.add_column("Rentals", style="white")
    for c in customers:
        table.add_row(c.name, c.email, c.phone or "N/A", str(len(c.rental_history)))
    console.print(table)

def display_cars(cars: list, available_only: bool = False):
    filtered = [c for c in cars if c.is_available()] if available_only else cars
    if not filtered:
        print_info("No vehicles found.")
        return
    title = "🚗 Available Vehicles" if available_only else "🚗 All Vehicles"
    table = Table(title=title, box=box.ROUNDED)
    table.add_column("Plate", style="bold magenta")
    table.add_column("Make", style="yellow")
    table.add_column("Model", style="cyan")
    table.add_column("Year", style="white")
    table.add_column("Category", style="blue")
    table.add_column("Rate/Day ($)", style="green")
    table.add_column("Status", style="white")
    for c in filtered:
        status = "[green]Available[/green]" if c.is_available() else "[red]Rented[/red]"
        table.add_row(c.plate, c.make, c.model, str(c.year), c.category, f"{c.rate_per_day:,.2f}", status)
    console.print(table)

def display_rentals(rentals: list):
    if not rentals:
        print_info("No rental records found.")
        return
    table = Table(title="📋 Rental Records", box=box.ROUNDED)
    table.add_column("Rental ID", style="bold white")
    table.add_column("Customer", style="yellow")
    table.add_column("Car Plate", style="cyan")
    table.add_column("Start Date", style="blue")
    table.add_column("Return Date", style="blue")
    table.add_column("Total Cost ($)", style="green")
    table.add_column("Status", style="white")
    for r in rentals:
        status = "[green]Returned[/green]" if r.status == "returned" else "[red]Active[/red]"
        table.add_row(r.rental_id, r.customer_email, r.car_plate, r.start_date,
                      r.return_date or "N/A", f"{r.total_cost:,.2f}", status)
    console.print(table)
