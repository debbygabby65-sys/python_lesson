def play_game():
    print("MYSTERY ISLAND: THE LOST LIGHTHOUSE.")
    print("A terrible storm has left you stranded on a mysterious island.")

    player_name = input("Enter your name: ")
    print(f"{player_name}, welcome to Mystery Island!")

    energy = 5
    current_location = "Beach"
    inventory = []

    print("Energy:", energy)
    print("Current location:", current_location)
    print("Inventory:", inventory)
    print("Your objective: escape Mystery Island by restoring the lighthouse beacon.")

    game_running = True

    while game_running:
        print("1. Explore the Jungle")
        print("2. Explore the Cave")
        print("3. Visit the Old Bridge")
        print("4. Visit the Lighthouse")
        print("5. Check Inventory")
        print("6. Quit Game")

        choice = input("What would you like to do? Enter a number: ")

        if choice == "1":
            print("You are exploring the jungle")
            energy -= 1
            print("Remaining energy:", energy)

            if energy <= 0:
                print("GAME OVER! You have run out of energy.")
                break

            current_location = "Jungle"
            print("New location:", current_location)

            if "Rope" not in inventory:
                inventory.append("Rope")
                print("The player found a rope")
            else:
                print("The player already has the rope")

        elif choice == "2":
            print("You are exploring the cave")
            energy -= 1
            print("Remaining energy:", energy)

            if energy <= 0:
                print("GAME OVER! You have run out of energy.")
                break

            current_location = "Cave"
            print("New location:", current_location)

            if "Lantern" not in inventory:
                inventory.append("Lantern")
                print("They found a lantern")
            else:
                print("They already have a lantern")

        elif choice == "3":
            print("You are approaching the Old Bridge")

            if "Rope" in inventory:
                print("They crossed safely")
                energy -= 1
                print("Remaining energy:", energy)

                if energy <= 0:
                    print("GAME OVER! You have run out of energy.")
                    break

                current_location = "Old Bridge"
                print("New location:", current_location)
            else:
                print("They need a rope")

        elif choice == "4":
            print("You are approaching the Lighthouse")

            if current_location == "Old Bridge":
                print("You have crossed the Old Bridge. Welcome to the Lighthouse!")

                if "Rope" in inventory and "Lantern" in inventory:
                    print("They can restore the lighthouse beacon")
                    print("Congratulations! You win!")
                    game_running = False
                else:
                    print("They need both items")
            else:
                print("You must cross the Old Bridge first.")

        elif choice == "5":
            print("Your inventory contains:")
            print(inventory)

        elif choice == "6":
            print("You have decided to leave Mystery Island. Game over!")
            game_running = False
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    return


play_again = "yes"

while play_again == "yes":
    play_game()
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()

print("Thanks for playing Mystery Island!")
