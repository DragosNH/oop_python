from character import Character
from races import Race
from spells import Spell

def main():
    aragorn = Character("Aragorn", Race.Human, "Ranger", "Sword", Spell.fire_ball, 100, 100)
    borromir = Character("Borromir", Race.Orc, "Ranger", "Sword", Spell.fire_ball, 100, 100)

    print(f"Before magic attack: {aragorn.mana_points}")

    print(aragorn.spell_attack(borromir))

    print(f"After magic attack: {aragorn.mana_points}")

if __name__ == "__main__":
    main()
