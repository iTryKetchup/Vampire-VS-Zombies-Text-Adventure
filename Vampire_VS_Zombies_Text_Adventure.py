def show_instructions():
    print("Vampires VS Zombies Text Adventure v0.01")
    print("Commands:")
    print("'go [direction]' to move")
    print("'inspect' to look around")
    print("'back' to return to the previous room")

def main():
    rooms = {'Rubble': {'east': 'cliffs', 'west': 'lake', 'south': 'desert', 'north': 'Burning City'}, 'cliffs': {'west': 'Rubble'}, 'lake': {'east': 'Rubble'}, 'desert': {'north': 'Rubble'}}
   
    current_room = 'Rubble'
    room_history = [current_room] 
    
    show_instructions()
    
    while True:
       command = input(">").strip().lower()
       
        if command in ['go east', 'go west', 'go north', 'go south']:
            direction = command.split()[1]
            if direction in rooms[current_room]:
               room_history.append(current room)
               current_room = rooms[current_room][direction]
            else:
               print("You have choosen wrong and a zombie is chasing you. Return to where you came from.")
               if len(room.history) > 1:
                  current_room = rooms_history.pop()
        elif command == 'back':
            if len (room_history) > 1:
               current_room = room_history.pop()
            else:
                print("No way back!")
        elif command == 'inspect':
                print(f"You are in the {current_room}")
            elif command == 'exit':
               break
        else:
            print("Invalid Command")
            
        print(f"Current Room: {current_room}")
       
if __name__ == "__main__":
    main()