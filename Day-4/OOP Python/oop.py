class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
            return f"The {self.make} {self.model}'s engine is running."

    def drive(self, distance):
        return f"The {self.make} {self.model} has driven {distance} miles."

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

# Access attributes and call methods of the objects
print(car1.make)        # Output: Toyota
print(car2.start_engine())    # Output: The Honda Civic's engine is running.
print(car1.drive(50))   # Output: The Toyota Camry has driven 50 miles.    
