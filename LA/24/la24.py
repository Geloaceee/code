LA#24
from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a Lightning!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an Bullet!")

warrior = Warrior()
mage = Mage()
marksman = Marksman()

warrior.attack()
mage.attack()
marksman.attack()

class Healer(GameCharacter):
    def attack(self):
        print("Casts a healing spell on ally!")

healer = Healer()
healer.attack()
