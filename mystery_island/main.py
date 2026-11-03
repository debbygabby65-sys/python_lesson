def play_game():
    print("====== MYSTERY ISLAND: THE LOST LIGHTHOUSE =====")
    print("A terrible storm has left you stranded on a mysterious island.")

    player_name = input("Enter your name: ")
    print(f"{player_name}, welcome to Mystery Island!")

    energy = 5
    current_location = "Beach"
    inventory = []
    bridge_crossed = False

    print("Energy:", energy)
    print("Current location:", current_location)
    print("Inventory:", inventory)

    print("Your objective: escape Mystery Island by restoring the lighthouse beacon.")

    game_running = True

    while game_running:
        print("========== GAME MENU ==========")
        print("1. Explore the Jungle")
        print("2. Explore the Cave")
        print("3. Visit the Old Bridge")
        print("4. Visit the Lighthouse")
        print("5. Check Inventory")
        print("6. Quit Game")

        choice = input("What would you like to do? Enter a number: ")

        if choice == "1":
            print("You are exploring the jungle.")
            print("1. Search the bushes")
            print("2. Follow the mysterious sound")

            jungle_choice = input("Enter your choice: ")

            if jungle_choice == "1":
                print("You found a hidden rope!")

                if "Rope" not in inventory:
                    inventory.append("Rope")
                    print("The Rope has been added to your inventory.")
                else:
                    print("You already have the Rope.")

            elif jungle_choice == "2":
                print("A wild animal chased you!")
                energy -= 1
                print("You lost an extra energy point.")

            else:
                print("Invalid jungle choice. No energy lost.")
            if jungle_choice == "1" or jungle_choice == "2":
                energy -= 1

                if energy <= 0:
                    energy = 0
                    print("Remaining energy:", energy)
                    print("GAME OVER! You have run out of energy.")
                    break
                print("Remaining energy:", energy)

                current_location = "Jungle"
                print("New location:", current_location)
       
       
        elif choice == "2":
            print("You are exploring the cave.")
            print("1. Search the dark corner.")
            print("2. Explore the narrow passage.")
            
            
            cave_choice = input("Enter your choice: ")
            
            if cave_choice == "1":
                if "Lantern" not in inventory:
                    inventory.append("Lantern")
                    print("You found a Lantern!")
                  
                else:
                    print("You already have the Lantern.")

                energy -= 1
            
            elif cave_choice == "2":
                print("Falling rocks! You lose 2 energy.")
                energy -= 2
            else:
                print("Invalid cave choice. No energy lost")
            if cave_choice == "1" or cave_choice == "2":
                if energy <= 0:
                    energy = 0
                    print("Remaining energy:", energy)
                    print("GAME OVER! You have run out of energy.")
                    break
                print("Remaining energy:", energy)
                current_location = "Cave"
                print("New location:", current_location)

        elif choice == "3":
            print("You are approaching the Old Bridge.")

            if "Rope" in inventory:
                print("1. Cross carefully.")
                print("2. Rush across.")

                bridge_choice = input("Enter your choice: ")

                if bridge_choice == "1":
                    print("You crossed safely using the Rope.")
                    energy -= 1

                elif bridge_choice == "2":
                    print("You rushed across and almost fell!")
                    energy -= 2

                else:
                    print("Invalid bridge choice. No energy lost.")

                if bridge_choice == "1" or bridge_choice == "2":
                    if energy <= 0:
                        energy = 0
                        print("Remaining energy:", energy)
                        print("GAME OVER! You have run out of energy.")
                        break
                    print("Remaining energy:", energy)
                    current_location = "Old Bridge"
                    bridge_crossed = True
                    print("New location:", current_location)

            else:
                print("You need a Rope to cross the Old Bridge.")
       
        elif choice == "4":
            print("You are approaching the Lighthouse.")
            if bridge_crossed:
                print("You have reached the Lighthouse!")

                if "Rope" in inventory and "Lantern" in inventory:
                    print("You used your Lantern to restore the lighthouse beacon!")
                    print("CONGRATULATIONS! YOU WIN!")
                    game_running = False

                else:
                    print("You need both the Rope and Lantern to restore the lighthouse.")

            else:
                print("You must cross the Old Bridge before reaching the Lighthouse.")
        
        elif choice == "5":
            print("========== INVENTORY ==========")
            print("Your items:", inventory)
            print("Remaining energy:", energy)
            print("Current location:", current_location)

        elif choice == "6":
            print("You have decided to leave Mystery Island.")
            game_running = False

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    print("Game session ended.")

if __name__ == "__main__":
    play_again = "yes"

    while play_again == "yes":
        play_game()
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()

    print("Thanks for playing Mystery Island!")