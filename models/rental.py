from datetime import datetime

class Rental:
    def __init__(self, rental_id: str, customer_email: str, car_plate: str, start_date: str = "", expected_return: str = ""):
        if not rental_id or not rental_id.strip():
            raise ValueError("Rental ID cannot be empty.")
        if not customer_email or not customer_email.strip():
            raise ValueError("Customer email cannot be empty.")
        if not car_plate or not car_plate.strip():
            raise ValueError("Car plate cannot be empty.")
        self.rental_id = rental_id.strip()
        self.customer_email = customer_email.strip()
        self.car_plate = car_plate.strip().upper()
        self.start_date = start_date or datetime.now().strftime("%Y-%m-%d")
        self.expected_return = expected_return
        self.return_date = None
        self.total_cost = 0.0
        self.status = "active"

    def process_return(self, rate_per_day: float, return_date: str = ""):
        self.return_date = return_date or datetime.now().strftime("%Y-%m-%d")
        self.status = "returned"
        try:
            start = datetime.strptime(self.start_date, "%Y-%m-%d")
            end = datetime.strptime(self.return_date, "%Y-%m-%d")
            days = max((end - start).days, 1)
            self.total_cost = round(days * rate_per_day, 2)
        except ValueError:
            self.total_cost = 0.0

    def to_dict(self) -> dict:
        return {"rental_id": self.rental_id, "customer_email": self.customer_email,
                "car_plate": self.car_plate, "start_date": self.start_date,
                "expected_return": self.expected_return, "return_date": self.return_date,
                "total_cost": self.total_cost, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict) -> "Rental":
        rental = cls(data["rental_id"], data["customer_email"], data["car_plate"],
                     data.get("start_date", ""), data.get("expected_return", ""))
        rental.return_date = data.get("return_date")
        rental.total_cost = data.get("total_cost", 0.0)
        rental.status = data.get("status", "active")
        return rental

    def __repr__(self):
        return f"Rental(id={self.rental_id}, car={self.car_plate}, status={self.status})"
