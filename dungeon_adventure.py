import random

def main():

    def setup_player():
        name = input("Enter your name: ")
        player = {
            "name": name,
            "health": 10,
            "inventory": []
        }
        return player


    def create_treasures():
        treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12)
        }
        return treasures


    def display_options(room_number):
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures):
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            item = random.choice(list(treasures.keys()))
            player["inventory"].append(item)
            print(f"You found a {item} worth {treasures[item]}!")

        else:
            player["health"] -= 2
            print("A trap! You lost 2 health.")


    def check_status(player):
        print(f"\nHealth: {player['health']}")

        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        total = 0
        for item in player["inventory"]:
            total += treasures[item]

        print("\n=== GAME OVER ===")
        print(f"Final Health: {player['health']}")

        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: None")

        print(f"Total Treasure Value: {total}")
        print("Game Over! Thanks for playing.")


    def run_game_loop(player, treasures):
        for room in range(1, 6):

            while True:
                display_options(room)
                choice = input("Choose an option (1-4): ")

                if choice == "1":
                    search_room(player, treasures)

                    if player["health"] <= 0:
                        print("\nYou ran out of health!")
                        end_game(player, treasures)
                        return

                elif choice == "2":
                    print("Moving to next room...")
                    break

                elif choice == "3":
                    check_status(player)

                elif choice == "4":
                    print("You chose to quit.")
                    end_game(player, treasures)
                    return

                else:
                    print("Invalid choice. Try again.")

        # After finishing all 5 rooms
        print("\nYou escaped the dungeon!")
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)


if __name__ == "__main__":
    main()
