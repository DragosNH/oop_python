class Character:
    def __init__(self, name, race, char_class, weapon, health_points, mana_points):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.weapon = weapon
        self.health_points = health_points
        self.mana_points = mana_points

    def __str__(self):
        return f"-------- Character --------\n \tName: {self.name}\n \tRace: {self.race}\n \tClass: {self.char_class}\n \tWeapon: {self.weapon}\n \tHP: {self.health_points}\n \tMP: {self.mana_points}"
