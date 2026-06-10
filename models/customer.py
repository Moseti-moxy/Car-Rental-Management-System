class Customer:
    def __init__(self, name: str, email: str, phone: str = ""):
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty.")
        if not email or not email.strip():
            raise ValueError("Customer email cannot be empty.")
        self.name = name.strip()
        self.email = email.strip()
        self.phone = phone.strip()
        self.rental_history = []

    def add_rental(self, rental_id: str):
        if rental_id not in self.rental_history:
            self.rental_history.append(rental_id)

    def to_dict(self) -> dict:
        return {"name": self.name, "email": self.email, "phone": self.phone, "rental_history": self.rental_history}

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        customer = cls(data["name"], data["email"], data.get("phone", ""))
        customer.rental_history = data.get("rental_history", [])
        return customer

    def __repr__(self):
        return f"Customer(name={self.name}, email={self.email})"
