from races import Race
from spells import Spell

# Constructor
class Character:
    def __init__(self, name, race, char_class, weapon, main_spell, health_points, mana_points):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.weapon = weapon
        self.main_spell = main_spell
        self.health_points = health_points + race.hp_bonus
        self.mana_points = mana_points + race.mp_bonus

    # Main attack
    def attack(self, target):
        target.health_points -= 10

        return f"{self.name} attaked {target.name}... {target.name} has {target.health_points} left"

    # Magic attack
    def spell_attack(self, target):
        target.health_points -= target.main_spell.spell_damage
        self.mana_points -= self.main_spell.spell_cost
        return f"{self.name} used {self.main_spell.spell_name} on {target.name}"

    # To string
    def __str__(self):
        return f"""
        -------- Character --------
        \tName: {self.name}
        \tRace: {self.race.race_name}
        \tClass: {self.char_class}
        \tWeapon: {self.weapon}
        \tMain Spell: {self.main_spell.spell_name}
        \tHP: {self.health_points}
        \tMP: {self.mana_points}
        """
