LA#20
class Adahbo:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat
        self._dryseason = dry_season
        self.__wetseason = wet_season
       
    def __str__(self):
        return f"Ang adahbo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
       
    def may_carrot_ba(self):
        return self.__wetseason
   
adahbong_dry = Adahbo("Siken", "watah", "sili")
Adahbo2 = Adahbo("Tilapia", "2big" , "asin")
Adahbo3 = Adahbo("Baboy", "water" , "Suka")
print(Adahbong_dry.may_carrot_ba())
print(Adahbo2.may_carrot_ba())
print(Adahbo3.may_carrot_ba())
