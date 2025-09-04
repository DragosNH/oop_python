from character import Character
from races import Race
from spells import Spell
from character_class import Character_class

def main():
    aragorn = Character("Aragorn", Race.Human, Character_class.warrior, "Sword", Spell.fire_ball, 100, 100)
    borromir = Character("Borromir", Race.Orc, Character_class.wizard, "Sword", Spell.ice_bolt, 100, 100)


    while borromir.health_points > 0 or aragorn.health_points > 0:
        if borromir.health_points <= 0 or aragorn.health_points <= 0:
            break
        print(aragorn.attack(borromir))
        print(f"---{borromir.name} has {borromir.health_points} left ---")
        print("--------------------------------")
        if borromir.mana_points < borromir.main_spell.spell_cost:
            break
        print(borromir.spell_attack(aragorn))
        print(f"---{aragorn.name} has {aragorn.health_points} HP left ---")
        print("--------------------------------")





if __name__ == "__main__":
    main()
