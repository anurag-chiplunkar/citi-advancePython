# Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return print("Vehicle Engine started.")


class Car(Vehicle):
    def __init__(self, model, brand, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def drive(self):
        return "Car is moving."


class Motorcycle(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model)
        self.num_wheels = num_wheels

    def ride(self):
        return "Motorcycle is riding."

car1 = Car(model="Honda", brand="Civic", num_doors=4)
car1.start_engine()