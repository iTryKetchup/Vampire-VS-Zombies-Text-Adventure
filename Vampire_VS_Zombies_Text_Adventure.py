import random

def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.02")
    print("Instructions:")
    print("'go [north, south, east, or west]' to move.")
    print("'pick up [item]' to add item to your inventory.")
    print("'use [item]' to use an item from your inventory.")
    print("'inventory' to check your items.")
    print("'inspect' to look around.")
    print("'back' to return to the previous room.")
    print("'exit' to quit the game.")
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
    print("Use the knife to defeat a vampire, Use the Bat to destroy a zombie.")
    
    rooms = {
        'Rubble': {
            'description': "You are in the Rubble, a desolate place with remnants of a once-thriving town. You see a bright light ahead.",
            'items': ['knife', 'bat'],
            'directions': {
                'east': 'Cliffs',
                'west': 'Lake',
                'south': 'Desert',
                'north': 'Burning City'
            },
            'directional_descriptions': {
                'east': "East towards the eerie Cliffs.",
                'west': "West to the misty Lake.",
                'south': "South into the hot Desert.",
                'north': "North towards the ominous Burning City."
            }
        },
        'Cliffs': {
            'description': "You are at the Cliffs, where you can hear the distant crashing of waves below.",
            'items': [],
            'enemy': 'vampire',
            'directional_descriptions': {
                'west': "Back west to the Rubble."
            }
        },
        'Lake': {
            'description': "You are by the Lake, its waters dark and foreboding. No way to cross visible.",
            'items': [],
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "Eastward leads back to Rubble."
            }
        },
        'Desert': {
            'description': "You are in the Desert, surrounded by endless sand under the scorching sun. No water or transportation around; try another route.",
            'items': [],
            'enemy': 'zombie',
            'directional_descriptions': {
                'north': "Northwards will take you back to Rubble."
            }
        },
        'Burning City': {
            'description': "You are in the Burning City, where the air is thick with smoke and the heat of smoldering ruins. Maybe underground will shelter you.",
            'items': [],
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to Sewers",
                'west': "West to Military Base",
                'south': "South to Rubble",
                'north': "North to Bowling Alley"
            }
        },
        'Military Base': {
            'description': "You are at a Military Base in ruins. It's a scary site with desolation in all directions.",
            'items': [],
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Burning City",
                'west': "West to More Lake",
                'south': "South to the Lake",
                'north': "North to The Chasm"
            }
        },
        'Bowling Alley': {
            'description': "You wander upon a Bowling Alley crawling with vampires and zombies.",
            'items': [],
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Mall",
                'west': "West to The Chasm",
                'south': "South to the Burning City",
                'north': "North to the Auto Park"
            }
        },
        'Sewers': {
            'description': "You are safe in the sewers. It smells, but you see another light in the depths of the sewer.",
            'items': [],
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Unknown",
                'west': "West to the Unknown",
                'south': "South to the Unknown",
                'north': "North to the Unknown"
            }
        },
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
                if direction in rooms[current_room].get('directions', {}):
                    room_history.append(current_room)
                    current_room = rooms[current_room]['directions'][direction]
                    if 'enemy' in rooms[current_room]:
                        print(f"You encounter a {rooms[current_room]['enemy']}!")
                else:
                    print("There is no path in this direction. Try another direction.")
            else:
                print("Please specify a direction to go.")
        elif command == 'back':
            if len(room_history) > 1:
                current_room = room_history.pop()
            else:
                print("No way back!")
        elif command == 'inspect':
            print(rooms[current_room]['description'])
            if rooms[current_room].get('directional_descriptions'):
                for direction, desc in rooms[current_room]['directional_descriptions'].items():
                    print(f"To the {direction}, {desc}")
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
        elif command.startswith('use '):
            item = command.split('use ')[1]
            if item in inventory:
                if 'enemy' in rooms[current_room]:
                    if (item == 'knife' and rooms[current_room]['enemy'] == 'vampire') or (item == 'bat' and rooms[current_room]['enemy'] == 'zombie'):
                        print(f"You have defeated the {rooms[current_room]['enemy']} with the {item}!")
                        rooms[current_room].pop('enemy')  # Remove the enemy from the room
                    else:
                        print("Wrong weapon chosen. Try again.")
                else:
                    print("There's nothing here to use that on.")
            else:
                print("You don't have that item in your inventory.")
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
