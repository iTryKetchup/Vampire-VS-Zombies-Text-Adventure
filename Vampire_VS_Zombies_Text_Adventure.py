import random

def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.10")
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
    print("Use the knife to defeat a vampire, Use the Bat to destroy a zombie, Firearms work on anything.")

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
            'directions': {
                'west': 'Rubble',
        },
            'enemy': 'vampire',
            'directional_descriptions': {
                'west': "Back west to the Rubble."
            }
        },
        'Lake': {
            'description': "You are by the Lake, its waters dark and foreboding. No way to cross visible.",
            'items': [],
            'directions': {
                'east': 'Rubble',
                'north': 'Military Base'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "Eastward leads back to Rubble."
            }
        },
        'Desert': {
            'description': "You are in the Desert, surrounded by endless sand under the scorching sun. No water or transportation around; try another route.",
            'items': [],
            'directions': {
                'north': 'Rubble'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'north': "Northwards will take you back to Rubble."
            }
        },
        'Burning City': {
            'description': "You are in the Burning City, where the air is thick with smoke and the heat of smoldering ruins. Maybe underground will shelter you.",
            'items': [],
            'directions': {
                'east': 'Sewers',
                'west': 'Military Base',
                'south': 'Rubble',
                'north': 'Bowling Alley'
            },
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
            'items': ['pistol'],
            'directions': {
                'east': 'Burning City',
                'west': 'River',
                'south': 'Lake',
                'north': 'Chasm'
            },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Burning City",
                'west': "West there is a raging River",
                'south': "South to the Lake",
                'north': "North to The Chasm"
            }
        },
        'River': {
            'description': "You are at River's edge.",
            'items': [],
            'directions': {
                'east': 'Military Base',
        },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Military Base",
                'west': "The river is too strong to cross",
                'south': "Downstream looks dangerous",
                'north': "Upstream looks unpassable"
            }
        },
        'Chasm': {
            'description': "You are at the edge of a vast Chasm.",
            'items': [],
            'directions': {
                'east': 'Bowling Alley',
                'south': 'Military Base'
        },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East to the Bowling Alley",
                'west': "West there is a raging River",
                'south': "South to the Military Base",
                'north': "North to a big hole"
            }
        },
        'Bowling Alley': {
            'description': "You wander upon a Bowling Alley crawling with vampires and zombies.",
            'items': [],
            'directions': {
                'west': 'Chasm',
                'south': 'Burning City'
            },
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
            'items': ['flashlight'],
            'directions': {
                'east': 'Subway Tunnel',
                'west': 'Burning City',
        },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "You see a faint light",
                'west': "West back to the Burning City",
                'south': "South is a wall",
                'north': "North is a wall"
            }
        },
        'Subway Tunnel': {
            'description': "You are in a subway tunnel it is very very Dark.",
            'items': [],
            'directions': {
                'east': 'Maintenance Tunnels',
                'west': 'Sewers',
        },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "Too dark to see.",
                'west': "Too dark to see.",
                'south': "Too dark to see.",
                'north': "Too dark to see."
            },
            'flashlight_descriptions': {
              'east': "East to the Maintenance Tunnels",
              'west': "West to the Sewers",
              'south': "South no access",
              'north': "North no access"
        },
  }}

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
              if item == 'flashlight' and 'flashlight_descriptions' in rooms[current_room]:
                print("You turn on the flashlight, revealing:")
                for direction, desc in rooms[current_room]['flashlight_descriptions'].items():
                    print(f"To the {direction}, {desc}")
              elif 'enemy' in rooms[current_room]:
                if  (item == 'knife' and rooms[current_room]['enemy'] == 'vampire') or\
                  (item == 'bat' and rooms[current_room]['enemy'] == 'zombie') or\
                  (item == 'pistol' and rooms[current_room]['enemy'] in ['vampire', 'zombie']):
                  print(f"You have defeated the {rooms[current_room]['enemy']} with the {item}!")
                  rooms[current_room].pop('enemy')
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
