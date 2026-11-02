print("MYSTERY ISLAND: THE LOST LIGHTHOUSE.")
print("A terrible storm has left you stranded on a mysterious island.")
player_name = input("Enter your name: ")
print(f"{player_name} Welcome to Mystery Island")

energy = 5
print("Energy:", energy)
current_location = "Beach"
print("Current location:", current_location)
inventory = []
print("Inventory:", inventory)
print("Your objective: escape Mystery Island by restoring the lighthouse beacon so a rescue boat can find you")

game_running = True
while game_running:
    print("1. Explore the Jungle")
    print("2. Explore the Cave")
    print("3. Visit the Old Bridge")
    print("4. Visit the Lighthouse")
    print("5. Check Inventory")
    print("6. Quit Game")

    choice = input("What would you like to do? Enter a number: ")
    print(choice)

    if choice == "1":
        print("You are exploring the jungle")
        energy -= 1
        print("Remaining energy:", energy) 
        if energy == 0:
            print("player has run out of energy")
            game_running = False
        current_location = "Jungle"
        print("New location:", current_location)
        if not "Rope" in inventory:
            inventory.append("Rope")
            print("The player found a rope")
        else:
            print("The player already has the rope")

    
    elif choice == "2":
        print("You are exploring the cave")
        current_location = "Cave"
        print("New location:", current_location)
        if not "Lantern" in inventory:
            inventory.append("Lantern")
            print("They found a lantern")
        else:
            print("They already have it ")

    elif choice == "3":
        print("You are approaching the Old Bridge")
    elif choice == "4":
        print("You are approaching the Lighthouse")
    elif choice == "5":
        print("Your inventory contains:")
    elif choice == "6":
        print("You have decided to leave Mystery Island. Game over!")
        game_running = False
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        