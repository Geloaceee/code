#LA10
class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        
    def describeVehicle(self):
        print(f"{self.brand} {self.model} uses {self.fuel_type} gas")

class Kotsi(Vehicle):
    pass

class Mowtor(Vehicle):
    pass

car1 = Kotsi("Ford", "F-150", "Gasoline")
car1.describeVehicle()
Meowtor = Mowtor("Kawasaki", "Ninja 400", "Gasoline")
Meowtor.describeVehicle()
