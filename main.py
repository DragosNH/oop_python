from character import Character
from races import Race
from spells import Spell

def main():
    aragorn = Character("Aragorn", Race.Human, "Ranger", "Sword", Spell.fire_ball, 100, 100)
    borromir = Character("Borromir", Race.Orc, "Ranger", "Sword", Spell.fire_ball, 100, 100)

    while borromir.health_points > 0:
        if aragorn.mana_points < aragorn.main_spell.spell_cost:
            break
        print(aragorn.spell_attack(borromir))


if __name__ == "__main__":
    main()
