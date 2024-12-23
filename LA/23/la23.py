LA#23
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing...")
            func()
            print("This character can one punch his enemy!")
        return wrapper

Saitama = AnimeCharacter("Saitama", "Fist")
@Saitama.introduce
def character_intro():
    print(f"I am {Saitama.name} and I can use {Fist.ability}.")

character_intro()
