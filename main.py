from character import Character
from races import Race

def main():
    aragorn = Character("Aragorn", Race.Human, "Ranger", "Sword", 100, 100)
    borromir = Character("Borromir", Race.Orc, "Ranger", "Sword",100, 100)

    print(aragorn.attack(borromir))
    print(borromir)

if __name__ == "__main__":
    main()
