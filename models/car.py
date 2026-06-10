class Car:
    CATEGORIES = ["Sedan", "SUV", "Truck", "Van", "Convertible", "Hatchback", "Other"]

    def __init__(self, plate: str, make: str, model: str, year: int, category: str = "Sedan", rate_per_day: float = 0.0):
        if not plate or not plate.strip():
            raise ValueError("Car plate cannot be empty.")
        if not make or not make.strip():
            raise ValueError("Car make cannot be empty.")
        if not model or not model.strip():
            raise ValueError("Car model cannot be empty.")
        self.plate = plate.strip().upper()
        self.make = make.strip()
        self.model = model.strip()
        self.year = int(year)
        self.category = category if category in self.CATEGORIES else "Other"
        self.rate_per_day = float(rate_per_day)
        self.status = "available"

    def mark_rented(self):
        self.status = "rented"

    def mark_available(self):
        self.status = "available"

    def is_available(self) -> bool:
        return self.status == "available"

    def to_dict(self) -> dict:
        return {"plate": self.plate, "make": self.make, "model": self.model,
                "year": self.year, "category": self.category,
                "rate_per_day": self.rate_per_day, "status": self.status}

    @classmethod
    def from_dict(cls, data: dict) -> "Car":
        car = cls(data["plate"], data["make"], data["model"], data["year"],
                  data.get("category", "Sedan"), data.get("rate_per_day", 0.0))
        car.status = data.get("status", "available")
        return car

    def __repr__(self):
        return f"Car({self.year} {self.make} {self.model}, plate={self.plate}, status={self.status})"
