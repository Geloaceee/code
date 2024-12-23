LA#5
class heroes:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def description(self, role, damage_type):
        print(f"{self.name} is a {role} that deals {damage_type} damage.")    

#init
super_hero = heroes("nana", "mage", "magic")  
print(f"{super_hero.name} is a {super_hero.role} that deals {super_hero.damage_type} damage.")
#desrcription
super_hero = heroes("chou", "fighter", "physical")
super_hero.description("fighter", "physical")
