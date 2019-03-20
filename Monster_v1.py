### Code for Animated Game: import pygame

floor_1 = ['nothing', 'sword', 'monster', 'magic stones', 'stairs up']
floor_2 = ['sword', 'stairs up', 'monster', 'nothing', 'stairs down']
floor_3 = ['sword', 'stairs down', 'nothing', 'boss monster', 'prize']

user_room = 0
pocket = []
floor_numbers = 0

print("There are seven differnet actions you can complete while on you journey to the prize.  The actions and their corresponding keys are listed below:\n 1. Left - L\n 2. Right - R\n 3. Up - U\n 4. Down - D\n 5. Grab - G\n 6. Fight - F\n 7. Help - H")
print("This game takes place in a three story dungeon.  The user has to traverse the levels in search of the prize. Along the way they collect items and fight monsters. On each move the user has seven possible commands: left, right, up, down, grab, fight, help. If the input is invalid (not one of these commands,) the game will let the user know. Otherwise, the game will execute the user's command. The goal of the game is to collect the prize guarded by the boss monster.")

user_input = input("What would you like to do? ")

if (floor_numbers == 0 and user_room == 2) or (floor_numbers == 1 and user_room == 2):
  monster = True
else:
  monster = False

if (floor_numbers == 0 and user_room == 4) or (floor_numbers == 1 and user_room == 1):
  stairs_up = True
else: 
  stairs_up = False
  
if (floor_numbers == 1 and user_room == 4) or (floor_numbers == 2 and user_room == 1):
  stairs_down = True
else:
  stairs_down = False

if floor_numbers == 0 and user_room == 3:
  stone = True
else:
  stone = False
  
if (floor_numbers == 0 and user_room == 1) or (floor_numbers == 2 and user_room == 1) or (floor_numbers == 3 and user_room == 1):
  sword = True
else:
  sword = False
  
if floor_numbers == 2 and user_room == 3:
  boss = True
else:
  boss = False
  
if user_input == 'l' and user_room == 0:
  print("You cannot move left.  This is the leftmost room on this floor.")
elif user_input == 'l' and user_room != 0:
  user_room -= 1
  
elif user_input == 'r':
  if user_room == 4:
    print("You cannot move right.  This is the rightmost room on this floor.")
    user_input = input("What would you like to do? ")
  elif user_room == 0:
    print("You are currently in the first room on floor " + str(floor_numbers))
    user_room += 1
    user_input = input("What would you like to do? ")
  elif user_room == 1:
    user_room += 1
    print("You are currently in the second room on floor " + str(floor_numbers)) 
    user_input = input("What would you like to do? ")
  elif user_room == 2:
    user_room += 1
    print("You are currently in the third room on floor " + str(floor_numbers))
    user_input = input("What would you like to do? ")
  elif user_room == 3:
    user_room += 1
    print("You are currently in the fourth room on floor " + str(floor_numbers))
    user_input = input("What would you like to do? ")
  elif monster == True:
    print("You cannot proceed to the next room without fighting the monster.")
    user_input = input("What would you like to do? ")
  
elif user_input == 'u':
  if stairs_up == True:
    floor_numbers += 1
    print("You are currently in room " + str(user_room) + "on floor " + str(floor_numbers))
    user_input = input("What would you like to do? ")
  else:
    print("You cannot move up in this location.  Search for a room or floor with an up staircase.")
    user_input = input("What would you like to do? ")
    
elif user_input == 'd':
  if stairs_down == True:
    user_room -= 1
    print("You are currently in room " + str(user_room) + "on floor " + str(floor_numbers))
    user_input = input("What would you like to do? ")
  else:
    print("You cannot move down in this location.  Search for a room or floor with a down staircase.")
    user_input = input("What would you like to do? ")
    
elif user_input == 'g':
  if stone == True and len(pocket) < 3:
    pocket.append("Some stones")
    user_input = input("What would you like to do? ")
  elif sword == True and len(pocket) < 3:
    pocket.append("A sword")
    user_input = input("What would you like to do? ")
  elif len(pocket) >= 3:
    print("Your pocket is already full.  You cannot pick up any new items at this time.")
    user_input = input("What would you like to do? ")
  else:
    print("There is nothing to grab in this room.  Either move to the next room or defeat the monster (if there is one).")
    user_input = input("What would you like to do? ")
  
        
elif user_input == 'f':
  if boss == True and ("A sword" in pocket and "Some stones" in pocket):
    print("You have beat the boss and won the final prize.")
  elif boss == False and "A sword" in pocket:
    print("You have beat this monster.")
    user_input = input("What would you like to do? ")
  elif boss == False and "Some stones" in pocket and len(pocket) <= 1:
    print("Sorry, you died because you didnt have a sword to fight with.  You will be taken back to the beggining of the game.")
    user_floor = 0
    user_room = 0
    user_input = input("What would you like to do? ")
  else:
    print("There is nothing to fight in this room.  Please continue with a different action.")
    user_input = input("What would you like to do? ")
    
elif user_input == 'h':
  print("This game takes place in a three story dungeon.  The user has to traverse the levels in search of the prize. Along the way they collect items and fight monsters. On each move the user has seven possible commands: left, right, up, down, grab, fight, help. If the input is invalid (not one of these commands,) the game will let the user know. Otherwise, the game will execute the user's command. The goal of the game is to collect the prize guarded by the boss monster.")
  print("There are seven differnet actions you can complete while on you journey to the prize.  The actions and their corresponding keys are listed below:\n 1. Left - L\n 2. Right - R\n 3. Up - U\n 4. Down - D\n 5. Grab - G\n 6. Fight - F\n 7. Help - H")
  user_input = input("What would you like to do? ")
