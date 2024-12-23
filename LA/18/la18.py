LA#18
class Sikenkeri:
    def __init__(self, meat,dry_season, wet_season):
        self.meat = meat
        self.dry_season = dry_season
        self.wet_season = wet_season
        
    
    def __str__(self):
        return f"Ang aking Sikenkeri ko ay {self.meat}, {self.dry_season}, { self.wet_season}"
    
Sikenkeri_dry = Sikenkeri("Siken", "wator", "powder")
Sikenkeri2 = Sikenkeri("Baboy", "wotoh" , "Dilis")
Sikenkeri3 = Sikenkeri("Baka", "water" , "Luya")
print(Sikenkeri_dry)
print(Sikenkeri2)
print(Sikenkeri3)
