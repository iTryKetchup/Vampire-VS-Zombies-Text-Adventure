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
    print("'help' to Show Instructions")
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

    rooms = { #every room is a unique location with a variety of items and enemies to battle, with an engaging story for our unknow hero
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
        'Groover Street': {
            'description': "You emerge into sunlight yet the feeling of dread still follows you.",
            'items': [],
            'directions': {
                'east': 'Skyscrapper',
                'north': 'Subway Station'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "East is a Skyscrapper with a broken barricade.",
                'west': "West there are hordes of zombies wandering about.",
                'south': "South you see Zombies swarming on something.",
                'north': "North towards the ominous Burning City."
            }
        },
        'Main Street': {
            'description': "You arrive at Main Street. it is eeriely quite.",
            'items': [],
            'directions': {
                'west': 'Subway Station',
                'south': 'Skyscrapper',
                'north': 'Collapsed Building'
            },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East is unknown from your position.",
                'west': "West is the Subway Station.",
                'south': "South to the Skyscrapper.",
                'north': "North towards a Collapsed Building."
            }
        },
        'Bus Depot': {
            'description': "You come upon an deserted Bus Depot, with no Busses any where in sight.",
            'items': ['rifle'],
            'directions': {
                'east': 'Franklin Street',
                'north': 'Tattered Cityscape'
            },
            'enemy': 'zombie',
            'enemy_on_inspect': 'vampire',
            'directional_descriptions': {
                'east': "East is Franklin Street.",
                'west': "West is crawling with Vampires.",
                'south': "South is crawling with zombies.",
                'north': "North towards the Tattered Cityscape."
            }
        },
        'Franklin Street': {
            'description': "You emerge onto Franklin Street.i",
            'entry_message': "Story Line 4\nStory Line 5\nStory Line 6",
            'items': [''],
            'directions': {
                'west': 'Bus Depot',
                'east': 'Collapsed Building',
                'south': 'Subway Station',
                'north': 'Fortified Grocery Store'
            },
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is a Collapsed Building.",
                'west': "West is the Bus Depot.",
                'south': "South is the Subway Station.",
                'north': "North towards a Fortified Grocery Store."
            }
        },
        'Collapsed Building': {
            'description': "You come across the remains of a Collapsed Building.",
            'items': [''],
            'directions': {
                'west': 'Franklin Street',
                'south': 'Main Street',
                'north': 'Rundown Motel'
            },
            'enemy': 'vampire',
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is a Zombie hordes.",
                'west': "West is Franklin Street.",
                'south': "South is Main Street.",
                'north': "North towards a Rundown Motel."
            }
        },
        'Tattered Cityscape': {
            'description': "You sneak up to see the Tattered Cityscape.",
            'items': [''],
            'directions': {
                'east': 'Fortified Grocery Store',
                'south': 'Bus Depot',
            },
            'enemy': 'zombie',
            'enemy_on_inspect': 'vampire',
            'directional_descriptions': {
                'east': "East is the Fortified Grocery Store.",
                'west': "West is a city on fire.",
                'south': "South is the Bus Depot.",
                'north': "North is hordes of Zombies."
            }
        },
        'Rundown Motel': {
            'description': "You come upon Rundown Motel. as you get closer you see a barricade made of dead bodies.",
            'items': [''],
            'directions': {
                'west': 'Fortified Grocery Store',
                'south': 'Collapsed Building'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "East is vast nothingness.",
                'west': "West is the Fortified Groery Store.",
                'south': "South is the Collapsed Building.",
                'north': "North is a gaggle of Vampires."
            }
        },
        'Fortified Grocery Store': {
            'description': "You come upon a demolished Fortified Grocery Store many old blood stains but no corpses.",
            'entry_message': "Story Line 7",
            'items': ['food'],
            'directions': {
                'west': 'Tattered Cityscape',
                'east': 'Rundown Motel',
                'south': 'Franklin Street',
                'north': 'Escape Tunnels'
            },
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is a Rundown Motel.",
                'west': "West is the Tattered Cityscape.",
                'south': "South is the Franklin Street.",
                'north': "North you see a hidden door towards a Escape Tunnel."
            }
        },
        'Power Generator': {
            'description': "You enter a very stuffy room with a massive Power Generator.",
            'items': [''],
            'directions': {
                'west': 'Armory',
                'south': 'Testing Lab'
            },
            'enemy': 'Vampire',
            'directional_descriptions': {
                'east': "East is nothing.",
                'west': "West is a sign for the Armory.",
                'south': "South is the Testing Lab.",
                'north': "North is nothing."
            }
        },
        'Armory': {
            'description': "You enter the Armory with many empty storage lockers and many locked cabinets.",
            'items': [''],
            'directions': {
                'west': 'Holding Cells',
                'east': 'Power Generator',
                'south': 'Underground Lab'
            },
            'enemy': 'vampire',
            'enemy_on_inspect': 'vampire',
            'directional_descriptions': {
                'east': "East is the Power Generator.",
                'west': "West is a sign for Holding Cells.",
                'south': "South is the Underground Lab.",
                'north': "North is nothing."
            }
        },
        'Holding Cells': {
            'description': "You with much forboding and see Holding Cells packed with Zombies.",
            'items': [''],
            'directions': {
                'east': 'Armory',
                'south': 'Incinerator Room'
            },
            'enemy': 'vampire',
            'enemy_on_inspect': 'vampire',
            'directional_descriptions': {
                'east': "East is the Armory.",
                'west': "West is nothing.",
                'south': "South is Incinerator Room.",
                'north': "North is nothing."
            }
        },
        'Incinerator Room': {
            'description': "You eneter a very Hot Incineraot Room.",
            'entry_message': "Story Line 12",
            'items': [''],
            'directions': {
                'west': 'Escape Tunnel',
                'east': 'Underground Lab',
                'south': 'Mysterious Room',
                'north': 'Escape Tunnels'
            },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East is the Underground Lab.",
                'west': "West you see a hidden door revealing a Hidden Tunnel.",
                'south': "South is the Mysterious Room.",
                'north': "North is a sign for Holding Cells."
            }
        },
        'Mysterious Room': {
            'description': "You enter a very Mysterious Room.",
            'entry_message': "Story Line 18",
            'items': [''],
            'directions': {
                'north': 'Incinerator Room'
            },
            'enemy': 'vampire',
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is nothing.",
                'west': "West is nothing.",
                'south': "South is nothing.",
                'north': "North is the Incinerator Room."
            }
        },
        'Hidden Tunnel': {
            'description': "You enter a very dark and dank Hidden Tunnel.",
            'items': [''],
            'directions': {
                'west': 'Basement',
                'east': 'Incinerator Room'
            },
            'directional_descriptions': {
                'east': "Too dark to see.",
                'west': "Too dark to see.",
                'south': "Too dark to see.",
                'north': "Too dark to see."
            },
            'flashlight_description': {
                'east': "You see the Incinerator Room",
                'west': "You see a faded sign saying Basement entrance",
                'south': "You see nothing",
                'north': "you see nothing"
            }
        },
        'Library': {
            'description': "You come upon a Library.",
            'items': [''],
            'directions': {
                'north': 'Basement'
            },
            'enemy': 'zombie',
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is herd of Zombies.",
                'west': "West is packs of Zombies.",
                'south': "South is hordes of Zombies.",
                'north': "North towards the Basement."
            }
        },
        'Basement': {
            'description': "You emerge from the tunnels into a well lit Basement.",
            'items': [''],
            'directions': {
                'east': 'Hidden Tunnel',
                'west': 'Police Station',
                'south': 'Library',
                'north': 'Hospital'
            },
            'enemy': 'vampire',
            'enemy_on_inspect': 'Vampire',
            'directional_descriptions': {
                'east': "East is the Hidden Tunnel.",
                'west': "West there is a sign for the Police Station.",
                'south': "South there is a sign for the Library.",
                'north': "North there is a sign for the Hospital."
            }
        },
        'Franklin Street': {
            'description': "You emerge to an empty Franklin Street.",
            'entry_message': "Story Line 4\nStory Line 5\nStory Line 6",
            'items': [''],
            'directions': {
                'west': 'Bus Depot',
                'east': 'Collapsed Building',
                'south': 'Subway Station',
                'north': 'Fortified Grocery Store'
            },
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is a Collapsed Building.",
                'west': "West is the Bus Depot.",
                'south': "South is the Subway Station.",
                'north': "North towards a Fortified Grocery Store."
            }
        },
        'Smoldering Building': {
            'description': "You come upon a Smoldering Building.",
            'items': [''],
            'directions': {
                'south': 'Hospital'
            },
            'enemy': 'Vampire',
            'directional_descriptions': {
                'east': "East is crawling with Vampires.",
                'west': "West is the Zombie Horde.",
                'south': "South is the Hospital.",
                'north': "North is the Zombie Horde."
            }
        },
        'Police Station': {
            'description': "You come upon a wreked Police Station.",
            'items': [''],
            'directions': {
                'east': 'Basement',
                'north': 'Eclipse Enclave'
            },
            'enemy': 'zombie',
            'enemy_on_inspect': 'zombie',
            'directional_descriptions': {
                'east': "East is the Basement.",
                'west': "West is the Zombie Horde.",
                'south': "South is the Zombie Horde.",
                'north': "North towards a Enclave."
            }
        },
        'Hospital': {
            'description': "You enter the Hosiptal Lobby and hear the faint cry for help in the distant cornor.",
            'entry_message': "Story Line 13",
            'items': [''],
            'directions': {
                'west': 'Eclipse Enclave',
                'south': 'Basement',
                'north': 'Smoldering Building'
            },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "East is a Zombie Horde.",
                'west': "West is an Enclave.",
                'south': "South is the Basement.",
                'north': "North towards Smoldering Building."
            }
        },
        'Eclipse Enclave': {
            'description': "You reached eclispe Enclave, and humans and Vampires seems to be work together.",
            'entry_message': "Story Line 14\nStory Line 15\nStory Line 16",
            'items': [''],
            'directions': {
                'east': 'Hospital',
                'south': 'Police Station'
            },
            'directional_descriptions': {
                'east': "East you see Humans defending the walls and Vampires preparing for to releave Humans at dusk.",
                'west': "West you see shops for food, electronics and internet cafes.",
                'south': "South is a makeshift Hospital with Humans lined up to donate blood.",
                'north': "North is a cage where Humans and Vampires seem to be training in combat."
            }
        },
        'Testing Lab': {
            'description': "You enter the Testing Lab with Zombies strapped to tables still wriggling around and medical devices whirlling around.",
            'entry_message': "Story Line 11",
            'items': [''],
            'directions': {
                'west': 'Underground Lab',
                'north': 'Power Generator'
            },
            'enemy_on_inspect': 'vampire',
            'directional_descriptions': {
                'east': "East is nothing.",
                'west': "West is the Underground Lab.",
                'south': "South is nothing.",
                'north': "North you see Power Generator sign."
            }
        },
        'Underground Lab': {
            'description': "You enter what looks like a medical research lab.",
            'entry_message': "Story Line 8\nStory Line 9\nStory Line 10",
            'items': ['Medicine'],
            'directions': {
                'west': 'Incinerator Room',
                'east': 'Testing Lab',
                'south': 'Escape Tunnel',
                'north': 'Armory'
            },
            'directional_descriptions': {
                'east': "East you see a sign for the Testing Lab.",
                'west': "West you see a sign for Incinerator Room.",
                'south': "South is an Escape Tunnel.",
                'north': "North you see a sign for the Armory."
            }
        },
        'Escape Tunnel': {
            'description': "You enter a very dark Escape Tunnel.",
            'entry_message': "Story Line 7",
            'items': [''],
            'directions': {
                'south': 'Fortified Grocery Store',
                'north': 'Underground Lab'
            },
            'directional_descriptions': {
                'east': "East is too dark to see.",
                'west': "West is too dark to see.",
                'south': "South is too dark to see.",
                'north': "North is too dark to see."
            },
            'flashlight_descriptions': {
              'east': "East is nothing",
              'west': "West is nothing",
              'south': "South reveals the Fortified Grocery Store",
              'north': "North reveals an Underground Lab sign"
            }
        },
        'Skyscrapper': {
            'description': "You come upon a demolished fortification many old blood stains but no corpses.",
            'items': ['rifle'],
            'directions': {
                'west': 'Groover Street',
                'north': 'Main Street'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "East is unknown from your position.",
                'west': "West is Groover Street.",
                'south': "South is crawling with zombies.",
                'north': "North towards Main Street."
            }
        },
        'Cliffs': {
            'description': "You are at the Cliffs, where you can hear the distant crashing of waves below.",
            'items': ['pistol'],
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
            'items': ['flashlight'],
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
            'enemy_on_inspect': 'zombie',
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
                'east': 'Train Tunnel',
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
        'Train Tunnel': {
            'description': "You are in a Train Tunnel it is very very Dark.",
            'items': [],
            'directions': {
                'east': 'Maintenance Tunnels',
                'west': 'Sewers'
            },
            'enemy': 'zombie',
            'enemy_on_inspect': 'vampire',
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
            }
        },
        'Maintenance Tunnels': {
            'description': "You have entered a dimly lit Maintenance Tunnels.",
            'items': [],
            'directions': {
                'east': 'Subway Station',
                'west': 'Train Tunnel',
            },
            'enemy': 'vampire',
            'directional_descriptions': {
                'east': "Too dark to see.",
                'west': "Too dark to see.",
                'south': "Too dark to see.",
                'north': "Too dark to see."
            },
            'flashlight_descriptions': {
              'east': "You see an exit sign",
              'west': "You see a sign Subway Tunnels wear a hard hat for entry",
              'south': "You see walls",
              'north': "You see walls"
            }
        },
        'Subway Station': {
            'description': "You emerge from the dark tunnels into a well lit Subway Station with resulting sounds in the distance",
            'items': [],
            'directions': {
                'east': 'Main Street',
                'west': 'Maintenance Tunnels',
                'south': 'Groover Street',
                'north': 'Franklin Street'
            },
            'enemy': 'zombie',
            'directional_descriptions': {
                'east': "You see a sign for Main Street",
                'west': "You see a sign for Maintenance Staff Only",
                'south': "You see a sign for Groover Street",
                'north': "You see a sign for Franklin Street"
            }
        }
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
                    if 'entry_message' in rooms[current_room]:
                        print(rooms[current_room]['entry_message'])
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
            if rooms[current_room]['items']:#shows loations items with inspect command
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
                        print(f"To the {direction}, {desc}")#will display new infoset with use flashight command at certain locations
                elif 'enemy' in rooms[current_room]:
                    if (item == 'knife' and rooms[current_room]['enemy'] == 'vampire') or\
                       (item == 'bat' and rooms[current_room]['enemy'] == 'zombie') or\
                       (item == 'rifle' and rooms[current_room]['enemy'] in ['vampire', 'zombie']) or\
                       (item == 'pistol' and rooms[current_room]['enemy'] in ['vampire', 'zombie']):
                        print(f"You have defeated the {rooms[current_room]['enemy']} with the {item}!")
                        rooms[current_room].pop('enemy')
                    else:
                        print(f"The {rooms[current_room]['enemy']} has killed you. Type restart to continue.")
                        print("Game Over!")
                        choice = input(">").strip().lower()
                        if choice == 'restart':
                            show_instructions()
                        elif choice == 'exit':
                            print("Thank you for playing! Goodbye!")
                        break
                else:
                    print("There's nothing here to use that on.")
            else:
                print("You don't have that item in your inventory.")
        elif command == 'inventory':
            if inventory:
                print("You have:", ", ".join(inventory))
            else:
                print("Your inventory is empty.")
        elif command == 'inspect':#extra function not working.Data added into rooms ready for activation
            print("You look around...")#enemy will appear when inspect command inputted
            if 'enemy_on_inspect' in rooms[current_room] and 'enemy' not in rooms[current_room]:
              enemy = rooms[current_room]['enemy_on_inspect']
              rooms[current_room]['enemy'] = enemy
              print(f"A {enemy} appears!")
        elif command == 'exit':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    show_instructions()
