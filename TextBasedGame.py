# Alyssa Osborne

# displays game instructions
def show_instructions():
    print("Nuclear Escape: Fruit Survival")
    print("Collect all 6 fruits to gain enough energy to defeat the radioactive monster")
    print("Move commands: go North, go South, go East, go West")
    print("------------------------------------------------")


# displays current room, inventory, and the item in the room
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in the {current_room} room")
    print(f"Inventory: {inventory}")

    # show item in room if there is one
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    print("------------------------------------------------")

# dictionary linking rooms, directions, and items
rooms = {
        'START': {'West': 'LAB', 'East': 'STORAGE', 'South': 'CENTRAL HUB'},  #start room
        'LAB': {'East': 'START', 'South': 'HAZARD', 'item': 'BANANA'},  # lab, banana
        'STORAGE': {'West': 'START', 'South': 'MED BAY', 'item': 'CHERRY'},  # storage, cherry
        'CENTRAL HUB': {'North': 'START', 'West': 'HAZARD', 'East': 'MED BAY', 'South': 'REACTOR', 'item': 'ORANGE'},  # central hub, orange
        'MED BAY': {'North': 'STORAGE', 'West': 'CENTRAL HUB', 'South': 'VAULT', 'item': 'GRAPES'},  # med bay, grapes
        'REACTOR': {'North': 'CENTRAL HUB', 'East': 'VAULT', 'item': 'APPLE'},  # reactor, apple
        'VAULT': {'North': 'MED BAY', 'West': 'REACTOR', 'item': 'PINEAPPLE'},  # vault, pineapple
        'HAZARD': {'East': 'CENTRAL HUB'}  # villain room
    }

current_room = 'START'
inventory = []

show_instructions()

# game loop
while True:
    show_status(current_room, inventory, rooms)

    move = input("Enter your move: ")
    move_parts = move.split()

    # validate input
    if len(move_parts) < 2:
        print("Invalid command!")
        continue

    command = move_parts[0]
    target = " ".join(move_parts[1:])

    # movement logic
    if command.lower() == 'go':
        direction = target.capitalize()

        if direction in rooms [current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    # item collection logic
    elif command.lower() == 'get':
        item = target.upper()

        if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
            inventory.append(item)
            del rooms[current_room]['item']
            print(f"{item} retrieved!")
        else:
            print("Can't get that item!")

    else:
        print("Invalid command!")


    # check win / lose
    if current_room == 'HAZARD':
        if len(inventory) == 6:
            print("\nYou feel energized from the fruit!")
            print("You defeat the radioactive monster and escape!")
            print("CONGRATULATIONS! YOU SURVIVED!")
        else:
            print("\nYou entered the HAZARD room without enough energy...")
            print("The radioactive monster consumes you.")
            print("GAME OVER!")
        break

