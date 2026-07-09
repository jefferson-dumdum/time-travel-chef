def main():
    print("=====================================")
    print("   THE TIME-TRAVELING CHEF")
    print("=====================================")
    print("You are a chef in 2024. You find a dusty ancient cookbook.")
    print("You open it and a time portal sucks you in!")
    print("You land in a historical kitchen. You see ONE weird ingredient.")
    print("Do you cook with: [1] A Giant Garlic Clove or [2] A Purple Carrot?")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou chose the Giant Garlic! You are sent to Ancient Rome...")
        print("You land in Caesar's kitchen. He is angry because his soup is bland.")
        print("You chop the giant garlic and toss it in. Caesar LOVES it!")
        print("He gives you a golden toga. You are now the Royal Chef of Rome.")
        print("THE END (Garlic Victory!)")
    elif choice == "2":
        print("\nYou chose the Purple Carrot! You are sent to the Viking Age...")
        # We will fill this in later on a branch!
        print("(To be continued on the 'carrot' branch...)")
    else:
        print("Invalid choice! The portal spits you back out. You lose.")

if __name__ == "__main__":
    main()