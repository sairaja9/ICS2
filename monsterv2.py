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

print("\nGame objective and dungeon:\nThis game takes place in a three story dungeon with floors 0, 1, 2 and rooms 0-4 in each floor.\nThe user has to traverse the floors and rooms in search of a prize.\nSome rooms have a staircase that goes up to a room in the floor above or a staircase that goes down to a room in a lower floor.\nThe game will end if the player grabs the prize.\nA room may have one of two types of monsters (a regular monster or a boss monster) that tries to kill the player, who has only three lives to give.\nAs the player searches a room for the prize, the rooms without the prize may contain a monster or an item such as a sword or stones.\nAs the player enters a room, they can see the content of that room.\nIf they grab a sword or stone from a room, the room content will then be updated to ‘nothing’.\n")
print("About the boss monster:\nThe boss monster guards the room that is before the room with the prize.\nThe player can slay the boss monster only by fighting the boss monster with a sword and some stones in their pocket.\nAfter the fight, the player will lose their sword and stones.\nIf the player is in need of a sword or a stone, the player can opt to not fight the regular monster or boss monster they may encounter in a room, and go back in the direction in which they came from to another room that may contain a sword or stone.\nEach monster has only one life to give.\nThe player cannot run past the boss monster guarding the room with the prize, or run past the last room in each floor.\n")
print("About the regular monsters:\nThe player can slay a regular monster by fighting them with a sword.\nAlthough the player slays the regular monster, they would lose the sword after their fight with the monster.\nAlso, the player can try to run past a regular monster with a 40 percent success rate.\nThe player will be caught by the monster and will consequently lose a life 60 percent of the time.\nIf a player loses three of their lives, the game ends without the player winning the prize.\n")
print("Valid inputs:\nThere are seven different actions or input that the player can complete while on their journey to the prize.\nThe actions and their corresponding keys on the keyboard are listed below:\n1. Left – l\n2. Right - r\n3. Up - u\n4. Down - d\n5. Grab - g\n6. Fight - f\n7. Run - run (you can run past regular monsters)\n8. Help - h\n9. Start - s (to start the game)\nAfter selecting an input, the player must press “enter” on keyboard. If the player selects an invalid input (i.e. not one of the above mentioned inputs or actions) the game will inform the player that the input is invalid.\nOtherwise, the game will execute the user’s command.\n")
print("Dungeon array display:\nAfter the player makes a move (i.e. action), the dungeon will be displayed as a 3x5 array.\nThe room that the player is not present in will be denoted by this: ' '.\nHence, if the player has not started the game, this will be the dungeon blueprint: The user's location in a specific room will be marked by an 'X'.\nThus, if the user is in floor 0, room 0, then the dungeon blueprint will be as follows: \n[' ', ' ', ' ', ' ', ' ']\n[' ', ' ', ' ', ' ', ' ']\n['X', ' ', ' ', ' ', ' '].\n")

board3 = [' ', ' ', ' ', ' ', ' ']
board2 = [' ', ' ', ' ', ' ', ' ']
board1 = [' ', ' ', ' ', ' ', ' ']
boards = [board3, board2, board1]

while start == True:
  user_input1 = input("Ready to play? If so, press s on the keyboard to start: ")
  if user_input1 == 's':
    init = True
    start = False
  else:
    print("You have entered an invalid command. Please enter one of the valid commands or press h to navigate to the help menu.")

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
      print("You have entered an invalid command. Please enter one of the valid commands or press h to navigate to the help menu.")
      
    elif user_input == 'run':
      if room_contents == 'monster' and user_room <= 3:
        runList = [1,2,3,4,5,6,7,8,9,10]
        temp = random.choice(runList)
        if temp <= 4:
          user_room += 1
          print(colored("You successfully ran past the monster", 'red'))
        else:
          print(colored("The monster caught you while you were running. You lost a life.", 'red'))
          board[user_room] = ' '
          floor_numbers = 0
          user_room = 0
          pocket = []
          lives -= 1
      else:
        print(colored("You cannot run past this room.", 'red'))

    if user_input == 'l':
        if user_room == 0:
          print(colored("You cannot move left. This is the leftmost room on this floor.", 'red'))
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
          print(colored("Sorry, you died because you didnt have a sword and some stones to fight the boss monster with. You lost a life.", 'red'))
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
          print(colored("Sorry, you died because you didnt have a sword to fight with. You lost a life.", 'red'))
          board[user_room] = ' '
          floor_numbers = 0
          user_room = 0
          pocket = []
          lives -= 1
        else:
          print(colored("There is nothing to fight in this room. Please continue with a different action.", 'red'))

    elif user_input == 'r':
        if user_room == 4:
            print(colored("You cannot move right. This is the rightmost room on this floor.", 'red'))
        elif win == False and (room_contents == 'monster' or room_contents == 'boss monster'):
          print(colored("You cannot pass this room without beating the monster.", 'red'))
        else:
            user_room += 1
        
    elif user_input == 'u':
        if room_contents == 'stairs up':
            board[user_room] = ' '
            floor_numbers += 1
        else:
            print(colored("You cannot move up in this location. Search for a room or floor with an up staircase.", 'red'))
        
    elif user_input == 'd':
        if room_contents == 'stairs down':
            board[user_room] = ' '
            floor_numbers -= 1
        else:
            print(colored("You cannot move down in this location. Search for a room or floor with a down staircase.", 'red'))
        
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
            print(colored("Your pocket is already full. You cannot pick up any new items at this time.", 'red'))
        else:
            print(colored("There is nothing to grab in this room.", 'red'))
        
    elif user_input == 'h':
      print("\nGame objective and about the dungeon where the game happens:\nThis game takes place in a three story dungeon with floors 0, 1, 2 and rooms 0-4 in each floor. The user has to traverse the floors and rooms in search of a prize. Some rooms have a staircase that goes up to a room in the floor above or a staircase that goes down to a room in a lower floor. The game will end if the player grabs the prize. A room may have one of two types of monsters (a regular monster or a boss monster) that tries to kill the player, who has only three lives to give. As the player searches a room for the prize, the rooms without the prize may contain a monster or an item such as a sword or stones. As the player enters a room, they can see the content of that room. If they grab a sword or stone from a room, the room content will then be updated to ‘nothing’.\n")
      print("About the boss monster:\nThe boss monster guards the room that is before the room with the prize. The player can slay the boss monster only by fighting the boss monster with a sword and some stones in their pocket. After the fight, the player will lose their sword and stones. If the player is in need of a sword or a stone, the player can opt to not fight the regular monster or boss monster they may encounter in a room, and go back in the direction in which they came from to another room that may contain a sword or stone. Each monster has only one life to give. The player cannot run past the boss monster guarding the room with the prize, or run past the last room in each floor.\n")
      print("About the regular monster:\nThe player can slay a regular monster by fighting them with a sword. Although the player slays the regular monster, they would lose the sword after their fight with the monster. Also, the player can try to run past a regular monster with a 40 percent success rate. The player will be caught by the monster and will consequently lose a life 60 percent of the time. If a player loses three of their lives, the game ends without the player winning the prize.\n")
      print("Dungeon array display:\nAfter the player makes a move (i.e. action), the dungeon will be displayed as a 3x5 array. The room that the player is not present in will be denoted by this: ' '. Hence, if the player has not started the game, this will be the dungeon blueprint: The user's location in a specific room will be marked by an 'X'. Thus, if the user is in floor 0, room 0, then the dungeon blueprint will be as follows: \n[' ', ' ', ' ', ' ', ' ']\n[' ', ' ', ' ', ' ', ' ']\n['X', ' ', ' ', ' ', ' '].\n")
      print("Valid inputs:\nThere are seven different actions or input that the player can complete while on their journey to the prize. The actions and their corresponding keys on the keyboard are listed below:\n1. Left – l\n2. Right - r\n3. Up - u\n4. Down - d\n5. Grab - g\n6. Fight - f\n7. Run - run (you can run past regular monsters)\n8. Help - h\n9. Start - s (to start the game)\nAfter selecting an input, the player must press “enter” on keyboard. If the player selects an invalid input (i.e. not one of the above mentioned inputs or actions) the game will inform the player that the input is invalid. Otherwise, the game will execute the user’s command.\n")
        
    elif lives <= 1:
      print("You lost all three of you lives. The game is over.")