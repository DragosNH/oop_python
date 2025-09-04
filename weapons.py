from enum import Enum

class Weapon(Enum):
    # name, damage, magic_damage, hp_bonus, mana_bonus
    sword = ("Sword", 5, 0, 5, 0)
    staff = ("Staff", 0, 5, 0, 5)
    hammer = ("Hammer", 2.5, 2.5, 2.5, 2.5)

    def __init__(self, weapon_name, main_damage, magic_damage, hp_bonus, mana_bonus):
        self.weapon_name = weapon_name
        self.main_damage = main_damage
        self.magic_damage = magic_damage
        self.hp_bonus = hp_bonus
        self.mana_bonus = mana_bonus

    def __str__(self):
        return self.weapon_name
