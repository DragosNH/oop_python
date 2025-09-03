from races import Race

class Character:
    def __init__(self, name, race, char_class, weapon, health_points, mana_points):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.weapon = weapon
        self.health_points = health_points + race.hp_bonus
        self.mana_points = mana_points + race.mp_bonus


    def attack(self, target):
        target.health_points -= 10

        return f"{self.name} attaked {target.name}... {target.name} has {target.health_points} left"

    def __str__(self):
        return f"-------- Character --------\n \tName: {self.name}\n \tRace: {self.race.value}\n \tClass: {self.char_class}\n \tWeapon: {self.weapon}\n \tHP: {self.health_points}\n \tMP: {self.mana_points}"
