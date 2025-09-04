from enum import Enum

class Spell(Enum):
    fire_ball = ("Fire ball", 10, 15)
    ice_bolt = ("Ice bolt", 5, 10)
    spark = ("Spark", 10, 15)

    def __init__(self, spell_name, spell_damage, spell_cost):
        self.spell_name = spell_name
        self.spell_damage = spell_damage
        self.spell_cost = spell_cost

    def __str__(self):
        return self.spell_name
