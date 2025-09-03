import Character

def main():
    aragorn = Character.Character("Aragorn", "Human", "Sword", "Ranger", 100, 100)
    borromir = Character.Character("Borromir", "Human", "Sword", "Ranger", 100, 100)

    print(aragorn.attack(borromir))

if __name__ == "__main__":
    main()
