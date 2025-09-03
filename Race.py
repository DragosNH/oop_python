from enum import Enum

class Race(Enum):
    Human = ("Human", 0, 0)
    Orc = ("Orc", 20, -10)
    Elf = ("Elf", -10, 20)

    def __init__(self, race_name, hp_bonus, mp_bonus):
        self.race_name = race_name
        self.hp_bonus = hp_bonus
        self.mp_bonus = mp_bonus

    def __str__(self):
        return self.race_name
