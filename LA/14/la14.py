#LA14
class Animal():
    def __init__(self, name, type, can_swim):
        self.name = name
        self.type = type

    def describeAnimal(self):
        print(f"{self.name} is a {self.type} that can swim, {self.can_swim}")
        

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        self.can_swim = True
        super().__init__(name, type, can_swim)

pshh = Fish("tapalia", "pshh", True)    
pshh.describeAnimal()
