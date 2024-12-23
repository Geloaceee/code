#LA7
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car_obj = Car("Toyota", "White")        
print(f"Original value: {car_obj.brand} , {car_obj.color}")

car_obj.color = "blue"
print(f"Original value: {car_obj.brand} , {car_obj.color}")

kotse = Car("Missubibi" , "Black")
print(f"Updated value: {kotse.brand} , {kotse.color}")
