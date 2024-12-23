#LA12
class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def describeToy(self):
        print(f"{self.name}, {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

kotse = Car("Honda", "500,000")
kotse.describeToy()
