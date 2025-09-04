from character import Character
from races import Race
from spells import Spell
from character_class import Character_class

def main():
    aragorn = Character("Aragorn", Race.Human, Character_class.warrior, "Sword", Spell.fire_ball, 100, 100)
    borromir = Character("Borromir", Race.Orc, Character_class.wizard, "Sword", Spell.fire_ball, 100, 100)

    print(aragorn)

    print(aragorn.attack(borromir))

"""
    while borromir.health_points > 0:
        if aragorn.mana_points < aragorn.main_spell.spell_cost:
            break
        print(aragorn.spell_attack(borromir))
"""


if __name__ == "__main__":
    main()
