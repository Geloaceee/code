class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} with {self.attack_power} damage")
        print(f"{target.name} has only {target.health} hp left")
        if target.health <= 0:
            print(f"The {target.name} is already defeated")
        
        
Mimasaur = Player("Mimasaur", 45, 8)
Salamander = Player("Salamander", 39, 6)

Mimasaur.attack(Salamander)
Salamander.attack(Mimasaur)

while Mimasaur.health > 0 and Salamander.health > 0:
    Mimasaur.attack(Salamander)
    if Salamander.health <= 0:
        print(f"{Mimasaur.name} wins!")
        break
    Salamander.attack(Mimasaur)
    if Mimasaur.health <= 0:
        print(f"{Salamander.name} wins!")
        break
    
    
    



        
        
        
        
        
