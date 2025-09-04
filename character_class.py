from enum import Enum

class Character_class(Enum):
    warrior = ("Warrior", 20, -5, 15, -10)
    wizard = ("Wizard", -5, 20, -10, 15)
    paladin = ("Paladin", 5, 5, 5, 5)

    def __init__(self, class_name, main_damage_bonus, magic_damage_bonus, health_bonus, mana_bonus):
        self.class_name = class_name
        self.main_damage_bonus = main_damage_bonus
        self.magic_damage_bonus = magic_damage_bonus
        self.health_bonus = health_bonus
        self.mana_bonus = mana_bonus

    def __str__(self):
        return self.class_name
