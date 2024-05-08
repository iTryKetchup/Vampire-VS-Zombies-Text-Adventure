import random

def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.02")
    print("Instructions.")
    print("'go [north, south, east or west]' to move")
    print("'pick up [item]' to add item to your inventory")
    print("'use [item]' to use an item from your inventory")
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
        'Rubble': {'description': "You are in the Rubble.", 'items': ['knife', 'bat'], 'east': 'Cliffs', 'west': 'Lake', 'south': 'Desert', 'north': 'Burning City'},
        'Cliffs': {'description': "You are at the Cliffs.", 'items': [], 'enemy': 'vampire'},
        'Lake': {'description': "You are by the Lake.", 'items': [], 'enemy': 'zombie'},
        'Desert': {'description': "You are in the Desert.", 'items': [], 'enemy': 'zombie'},
        'Burning City': {'description': "You are in the Burning City.", 'items': [], 'enemy': 'vampire'},
    }
    
    inventory = []
    current_room = 'Rubble'
    room_history = [current_room]

    while True:
        command = input(">").strip().lower()
        
        if command.startswith('go '):
            parts = command.split()
            if len(parts) > 1:
                direction = parts[1]
                if direction in rooms[current_room]:
                    room_history.append(current_room)
                    current_room = rooms[current_room][direction]
                    if 'enemy' in rooms[current_room]:
                        print(f"You encounter a {rooms[current_room]['enemy']}!")
                else:
                    print("You cannot go that way. A zombie might be waiting!")
                    if len(room_history) > 1:
                        current_room = room_history.pop()
            else:
                print("Please specify a direction to go.")
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
            parts = command.split('pick up ')
            if len(parts) > 1:
                item = parts[1]
                if item in [i.lower() for i in rooms[current_room]['items']]:  # Case-insensitive match
                    inventory.append(item)
                    rooms[current_room]['items'].remove(item)
                    print(f"You picked up a {item}.")
                else:
                    print(f"There is no {item} here.")
            else:
                print("Please specify an item to pick up.")
        elif command.startswith('use '):
            parts = command.split('use ')
            if len(parts) > 1:
                item = parts[1]
                if item in inventory and 'enemy' in rooms[current_room]:
                    if (item == 'knife' and rooms[current_room]['enemy'] == 'zombie') or (item == 'bat' and rooms[current_room]['enemy'] == 'vampire'):
                        print(f"You have defeated the {rooms[current_room]['enemy']} with the {item}!")
                        rooms[current_room].pop('enemy')  # Remove the enemy from the room
                    else:
                        print(f"The {item} has no effect on the {rooms[current_room]['enemy']}.")
                else:
                    print("You can't use that here.")
            else:
                print("Please specify an item to use.")
        elif command == 'inventory':
            if inventory:
                print("You have:", ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif command == 'exit':
            print("Thank you for playing! Goodbye!")
            break
                
if __name__ == "__main__":
    show_instructions()
