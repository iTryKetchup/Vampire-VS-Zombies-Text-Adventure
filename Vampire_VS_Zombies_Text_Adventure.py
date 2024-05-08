def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.02")
    print("Instructions.")
    print("'go [north, south, east or west]' to move")
    print("'pick up [item]' to add item to your inventory")
    print("'inventory' to check your items")
    print("'inspect' to look around")
    print("'back' to return to previous room")
    print("'exit' to quit the game")
    print("\nType 'start' to begin your adventure or 'exit' to quit.")
    
    while True:
        command = input(">").strip().lower()
        if command == 'start':
            start_game()
            break
        elif command == 'exit':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Did you type that correctly? Please type 'start' to begin or 'exit' to quit.")

def start_game():
    print("Story Line 1")
    print("Story Line 2")
    print("Story Line 3")
    
    rooms = {
        'Rubble': {'description': "You are in the Rubble.", 'items': ['map', 'flashlight'], 'east': 'Cliffs', 'west': 'Lake', 'south': 'Desert', 'north': 'Burning City'},
        'Cliffs': {'description': "You are at the Cliffs.", 'items': ['rope'], 'west': 'Rubble'},
        'Lake': {'description': "You are by the Lake.", 'items': ['water bottle'], 'east': 'Rubble'},
        'Desert': {'description': "You are in the Desert.", 'items': ['sun hat'], 'north': 'Rubble'},
        'Burning City': {'description': "You are in the Burning City.", 'items': ['fire extinguisher'], 'east': 'Sewers', 'west': 'Military Base', 'south': 'Rubble', 'north': 'Bowling Alley'},
    }
    
    inventory = []

    current_room = 'Rubble'
    room_history = [current_room]

    while True:
        command = input(">").strip().lower()
        
        if command.startswith('go '):
            direction = command.split()[1]
            if direction in rooms[current_room]:
                room_history.append(current_room)
                current_room = rooms[current_room][direction]
            else:
                print("You cannot go that way. A zombie might be waiting!")
                if len(room_history) > 1:
                    current_room = room_history.pop()
        elif command == 'back':
            if len(room_history) > 1:
                current_room = room_history.pop()
            else:
                print("No way back!")
        elif command == 'inspect':
            print(rooms[current_room]['description'])
            if rooms[current_room]['items']:
                print("You see here:", ", ".join(rooms[current_room]['items']))
        elif command.startswith('pick up '):
            item = command.split('pick up ')[1]
            if item in rooms[current_room]['items']:
                inventory.append(item)
                rooms[current_room]['items'].remove(item)
                print(f"You picked up a {item}.")
            else:
                print(f"There is no {item} here.")
        elif command == 'inventory':
            if inventory:
                print("You have:", ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif command == 'exit':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Unknown command! Try Again!")
            
        print(f"Current Room: {current_room}")
        
if __name__ == "__main__":
    show_instructions()
