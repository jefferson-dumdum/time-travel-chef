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
        # We will fill this in later on a branch!
        print("(To be continued on the 'garlic' branch...)")
    elif choice == "2":
        print("\nYou chose the Purple Carrot! You are sent to the Viking Age...")
        print("You land in a longhouse. The Vikings are confused by the purple veggie.")
        print("You roast it over the fire and serve it with honey.")
        print("The Vikings cheer! They name you 'Carrot-Slayer' and give you a ship.")
        print("THE END (Carrot Victory!)")

if __name__ == "__main__":
    main()