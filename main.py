from character import Character
from races import Race
from spells import Spell
from character_class import Character_class
from weapons import Weapon


def main():
    aragorn = Character("Aragorn", Race.Human, Character_class.warrior, Weapon.sword, Spell.fire_ball, 100, 100)
    orcomir = Character("Orcomir", Race.Orc, Character_class.wizard, Weapon.staff, Spell.ice_bolt, 100, 100)


    while orcomir.health_points > 0 or aragorn.health_points > 0:
        if orcomir.health_points <= 0 or aragorn.health_points <= 0:
            break
        print(aragorn.attack(orcomir))
        print(f"---{orcomir.name} has {orcomir.health_points} left ---")
        print("--------------------------------")
        if orcomir.mana_points < orcomir.main_spell.spell_cost:
            break
        print(orcomir.spell_attack(aragorn))
        print(f"---{aragorn.name} has {aragorn.health_points} HP left ---")
        print("--------------------------------")





if __name__ == "__main__":
    main()
