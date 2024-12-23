#LA9
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return (f"{self.brand} is a car brand.")    
    
kotchi = Car("Toyota")
print(kotchi.brand)
del kotchi
print(kotchi)
