LA#19
class Paksiw:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat
        self._dryseason = dry_season
        self.__wetseason = wet_season
        
    def __str__(self):
        return f"Ang Paksiw ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
    
Paksiwna_dry = Paksiw("tilapia", "water", "suka")
Paksiw2 = Paksiw("tipaklong", "watah" , "sapsap")
Paksiw3 = Paksiw("talong", "water" , "pinya")
print(Paksiwna_dry.__meat)
print(Paksiw2.__dryseason)
print(Paksiw3.__wetseason)

