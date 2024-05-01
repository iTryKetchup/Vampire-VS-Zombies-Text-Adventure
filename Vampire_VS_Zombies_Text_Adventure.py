def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.01")
    print("Commands:")
    print("'go [north, south, east or west]' to move")
    print("'inspect' to look around")
    print("'back' to return to the previous room")
    print("'exit' to quit the game")
    print('\nType 'start' to begin your adventure or "exit' to quit:")
    
    def start_game():
        print("Enter Text")
        print("Enter Text 2")
        print("Enter Text 3")
        show_instrutions()
        
        rooms = {
            'Rubble': {'east': 'cliffs', 'west': 'lake', 'south': 'desert', 'north': 'Burning City'}, 
            'cliffs': {'west': 'Rubble'}, 
            'lake': {'east': 'Rubble'}, 
            'desert': {'north': 'Rubble'}
            'Burning City': {'east': 'Sewers', 'west': 'Military Base', 'south': 'rubble', 'north': 'Bowling Alley'),
    }
   
    current_room = 'Rubble'
    room_history = [current_room]
    
    while True:
       command = input(">").strip().lower()
       
       if command in ['go east', 'go west', 'go north', 'go south']:
            direction = command.split()[1]
            if direction in rooms[current_room]:
               room_history.append(current_room) 
               current_room = rooms[current_room][direction]
            else:
               print("You have choosen wrong and a zombie is chasing you. Return to where you came from.")
               if len(room_history) > 1: 
                  current_room = room_history.pop()
       elif command == 'back':
            if len(room_history) > 1:
               current_room = room_history.pop()
            else:
                print("No way back!")
       elif command == 'inspect':
                print(f"You are in the {current_room}")
       elif command == 'exit':
               break
       else:
            print("That was a BAD choice! Try Again!")
            
       print(f"Current Room: {current_room}")
       
if __name__ == "__main__":
    show_instructions()
