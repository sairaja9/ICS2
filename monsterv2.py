from termcolor import colored
import random

floor1 = ['stairs up', 'sword', 'monster', 'stones', 'nothing']
floor2 = ['stairs down', 'stairs up', 'sword', 'monster', 'monster']
floor3 = ['sword', 'stairs down', 'nothing', 'boss monster', 'prize']
floors = [floor1, floor2, floor3]
user_input_list = ['l','r','u','d','g','f','run','h']

user_room = 0
pocket = []
floor_numbers = 0
lives = 3
win = False
run = False
init = False
start = True

print("There are seven differnet actions you can complete while on your journey to the prize.  The actions and their corresponding keys are listed below:\n 1. Left - l\n 2. Right - r\n 3. Up - u\n 4. Down - d\n 5. Grab - g\n 6. Fight - f\n 7. Run - run (you can run past regular monsters)\n 8. Help - h\n 9. Start - s (to start the game)")
print("This game takes place in a three story dungeon.  Each floor has five rooms.  The user has to traverse the levels in search of the prize. Along the way they collect items and fight monsters. On each move the user has nine possible commands: left, right, up, down, grab, fight, run, help, start. If the input is invalid (not one of these commands,) the game will let the user know. Otherwise, the game will execute the user's command. The goal of the game is to collect the prize guarded by the boss monster.")
board3 = [' ', ' ', ' ', ' ', ' ']
board2 = [' ', ' ', ' ', ' ', ' ']
board1 = [' ', ' ', ' ', ' ', ' ']
boards = [board3, board2, board1]
print("This is the dungeon blueprint:")
print(board1)
print(board2)
print(board3)

while start == True:
  user_input1 = input("Press s to start: ")
  if user_input1 == 's':
    init = True
    start = False
  else:
    print("You have entered an invalid command.  Please enter one of the valid commands or press h to navigate to the help menu.")

while init == True and lives >= 1:
    current_floor = floors[floor_numbers]
    room_contents = current_floor[user_room]
    print(colored("You are currently in room " + str(user_room) + " on floor " + str(floor_numbers), 'green'))
    board = boards[floor_numbers]
    board[user_room] = 'X'
    board[user_room -1] = ' '
    print(board1)
    print(board2)
    print(board3)
    print(colored("This room has: " + room_contents, 'yellow'))
    print(colored("This is what you have in your pocket " + str(pocket), 'green'))
    user_input = input("What would you like to do? ")
    
    if user_input not in user_input_list:
      print("You have entered an invalid command.  Please enter one of the valid commands or press h to navigate to the help menu.")
      
    elif user_input == 'run':
      if room_contents == 'monster' and user_room <= 3:
        runList = [1,2,3,4,5,6,7,8,9,10]
        temp = random.choice(runList)
        if temp <= 4:
          user_room += 1
          print(colored("You successfully ran past the monster", 'red'))
        else:
          print(colored("The monster caught you while you were running.  You lost a life.", 'red'))
          board[user_room] = ' '
          floor_numbers = 0
          user_room = 0
          pocket = []
          lives -= 1
      else:
        print(colored("You cannot run past this room.", 'red'))

    if user_input == 'l':
        if user_room == 0:
          print(colored("You cannot move left.  This is the leftmost room on this floor.", 'red'))
        else:
          board[user_room] = ' '
          user_room -= 1
            
    elif user_input == 'f':
        if room_contents == 'boss monster' and ("A sword" in pocket and "Some stones" in pocket):
          print(colored("You have beat the boss monster.", 'red'))
          current_floor.remove('boss monster')
          current_floor.insert(user_room, 'nothing')
          pocket.remove("A sword")
          pocket.remove("Some stones")
          win = True
        elif room_contents == 'boss monster' and ("A sword" not in pocket and "Some stones" not in pocket):
          print(colored("Sorry, you died because you didnt have a sword and some stones to fight the boss monster with.  You lost a life.", 'red'))
          board[user_room] = ' '
          floor_numbers = 0
          user_room = 0
          pocket = []
          lives -= 1
        elif room_contents == 'monster' and "A sword" in pocket:
          print(colored("You have beat this monster.", 'red'))
          current_floor.remove('monster')
          current_floor.insert(user_room, 'nothing')
          pocket.remove("A sword")
          win = True
        elif room_contents == 'monster' and "A sword" not in pocket:
          print(colored("Sorry, you died because you didnt have a sword to fight with.  You lost a life.", 'red'))
          board[user_room] = ' '
          floor_numbers = 0
          user_room = 0
          pocket = []
          lives -= 1
        else:
          print(colored("There is nothing to fight in this room.  Please continue with a different action.", 'red'))

    elif user_input == 'r':
        if user_room == 4:
            print(colored("You cannot move right.  This is the rightmost room on this floor.", 'red'))
        elif win == False and (room_contents == 'monster' or room_contents == 'boss monster'):
          print(colored("You cannot pass this room without beating the monster.", 'red'))
        else:
            user_room += 1
        
    elif user_input == 'u':
        if room_contents == 'stairs up':
            board[user_room] = ' '
            floor_numbers += 1
        else:
            print(colored("You cannot move up in this location.  Search for a room or floor with an up staircase.", 'red'))
        
    elif user_input == 'd':
        if room_contents == 'stairs down':
            board[user_room] = ' '
            floor_numbers -= 1
        else:
            print(colored("You cannot move down in this location.  Search for a room or floor with a down staircase.", 'red'))
        
    elif user_input == 'g':
        if room_contents == 'stones' and len(pocket) < 3:
          pocket.append("Some stones")
          current_floor.remove('stones')
          current_floor.insert(user_room, 'nothing')
        elif room_contents == 'sword' and len(pocket) < 3:
          pocket.append("A sword")
          current_floor.remove('sword')
          current_floor.insert(user_room, 'nothing')
        elif room_contents == 'prize' and len(pocket) < 3:
          pocket.append("Final Prize")
          print("You have beat the boss monster and won the final prize.")
          init = False
        elif len(pocket) >= 3:
            print(colored("Your pocket is already full.  You cannot pick up any new items at this time.", 'red'))
        else:
            print(colored("There is nothing to grab in this room.", 'red'))
        
    elif user_input == 'h':
        print("This game takes place in a three story dungeon. Each room has five floors. The user has to traverse the levels in search of the prize. Along the way they collect items and fight monsters. On each move the user has nine possible commands: left, right, up, down, grab, fight, help, start. If the input is invalid (not one of these commands,) the game will let the user know. Otherwise, the game will execute the user's command. The goal of the game is to collect the prize guarded by the boss monster.")
        print("There are seven differnet actions you can complete while on you journey to the prize.  The actions and their corresponding keys are listed below:\n 1. Left - l\n 2. Right - r\n 3. Up - u\n 4. Down - d\n 5. Grab - g\n 6. Fight - f\n 7. Run - run (you can run past regular monsters)\n 8. Help - h\n 9. Start - s(to start the game)")
        
    elif lives <= 1:
      print("You lost all three of you lives. The game is over.")