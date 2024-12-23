LA#26
from abc import ABC, abstractmethod

class PowerRangers(ABC):
    @property
    @abstractmethod
    def alias(self):
        pass

class Red(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"
   
class Yellow(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

class Blue(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"
   
class Pink(PowerRangers):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.__alias = __alias

    @property
    def alias(self):
        return f"{self.real_name}, {self.__alias}"

import oop

red = oop.Red("Red", "Redflag")
yellow = oop.Yellow("Yellow", "Yellowflag")
blue = oop.Blue("Blue", "Bluesky")
pink = oop.Pink("Pink", "pinkflag")

print(red.alias)
print(yellow.alias)
print(blue.alias)
print(pink.alias)
