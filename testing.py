'''
if user_input == run:
    if room_contents == monster:
        if room_contents == 'monster' and user_room >= 1:
            runList = [1,2,3,4,5,6,7,8,9,10]
            temp = random.choice(runList)
        if temp <= 4:
            user_room -= 1
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
'''