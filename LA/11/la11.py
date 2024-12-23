#LA11
class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describePhone(self):
        print(f"{self.brand} {self.model}")
        

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
        
silpon = Android("Oppo", "reno 11 pro 5g")  
silpon.describePhone()
