LA#21
class  Adahbo:
    def __init__(self, meat, dry_season, wet_season):
        self.meat = meat                
        self._dryseason = dry_season    
        self.__wetseason = wet_season   
        
    def __str__(self):
        return f"Ang  Adahbo ko ay {self.meat}, {self._dryseason}, {self.__wetseason}"
        
    def may_carrot_ba(self):
        return self.__wetseason
        
    def set_carrot(self, bagong_value):
        self.__wetseason = bagong_value
    
Adahbong_dry = Adahbo("Siken", "watah", "sili")
Adahbo2 = Adahbo("Tilapia", "2big" , "asin")
Adahbo3 = Adahbo("Baboy", "water" , "Suka")
Adahbong_dry.set_carrot("new carrot 1")
Adahbo2.set_carrot("new carrot 2")
Adahbo3.set_carrot("new carrot 3")
print(Adahbong_dry.may_carrot_ba())
print(Adahbo2.may_carrot_ba())
print(Adahbo3.may_carrot_ba())
