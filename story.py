def main():
    print("=====================================")
    print("   THE TIME-TRAVELING CHEF")
    print("=====================================")
    print("You are a chef in 2024. You find a dusty ancient cookbook.")
    print("You open it and a time portal sucks you in!")
    print("You land in a historical kitchen. You see ONE weird ingredient.")
    print("Do you cook with: [1] A Giant Garlic Clove or [2] A Purple Carrot?")
    print("Or maybe: [3] A Mysterious Spicy Chili?")
    
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nYou chose the Giant Garlic! You are sent to Ancient Rome...")
        print("You land in Caesar's kitchen. He is angry because his soup is too salty.")
        print("You chop the giant garlic and toss it in. Caesar LOVES it!")
        print("He gives you a golden toga. You are now the Royal Chef of Rome.")
        print("THE END (Garlic Victory!)")
    elif choice == "2":
        print("\nYou chose the Purple Carrot! You are sent to the Viking Age...")
        print("You land in a longhouse. The Vikings are confused by the purple veggie.")
        print("You roast it over the fire and serve it with honey.")
        print("The Vikings cheer! They name you 'Carrot-Slayer' and give you a ship.")
        print("THE END (Carrot Victory!)")
    elif choice == "3":
        print("\nYou chose the Mysterious Spicy Chili! You are sent to Ancient China...")
        print("You land in the Emperor's palace. He wants a dish with 'fire' in it.")
        print("You grind the chili and add it to his noodles. The Emperor LOVES it!")
        print("He gives you a silk robe and names you 'The Fire Chef of the East'.")
        print("THE END (Chili Victory!)")
    else:
        print("Invalid choice! The portal spits you back out. You lose.")

if __name__ == "__main__":
    main()