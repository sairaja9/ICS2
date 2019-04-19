import functions
import auto
import AI
import variables

# Simulation game of traveling out west in 1800's

# The main program. No need to modify anything below here.

print(functions.text.welcome_text + functions.text.help_text + functions.text.good_luck_text)
player_name = input("\nWhat is your name, player?: ")

while variables.playing:
    print()
    ########## Normal Game Player ##########
    #action = input("Choose an action, {0} -->".format(player_name))
    ##########

    ########## Extra Credit/ AI/ Smart Player ##########
    action = AI.choose_action()
    ##########

    ########## Extra Credit/ Auto Player ##########
    #action = auto.auto_action
    ##########
    if action == "travel" or action == "t":
        functions.handle_travel()
    elif action == "rest" or action == "r":
        functions.handle_rest()
    elif action == "hunt" or action == "h":
        functions.handle_hunt()
    elif action == "quit" or action == "q":
        functions.handle_quit()
    elif action == "help" or action == "?":
        functions.handle_help()
    elif action == "status" or action == "s":
        functions.handle_status()
    else:
        functions.handle_invalid_input(action)

    if functions.game_is_over():
        variables.playing = False

if functions.player_wins():
    print("\n\nCongratulations you made it to Oregon alive!")
    functions.handle_status()
else:
    print("\n\nAlas! You lose.")
    functions.handle_status()
    print(functions.loss_report())