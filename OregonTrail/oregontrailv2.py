# Simulation game of traveling out west in 1800's

import random

welcome_text = """
Welcome to the Oregon Trail! Your goal is to travel by wagon
train from New York City to Oregon (2000 miles). You start on
March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You
can hunt and rest, but you have to get there before winter!
"""

help_text = """
Each turn you can take one of 3 actions:

  travel - moves you randomly between 30-60 miles and takes
           3-7 days (random).
  rest   - increases health 1 level (up to 5 maximum) and takes
           2-5 days (random).
  hunt   - adds 100 lbs of food and takes 2-5 days (random).

When prompted for an action, you can also enter one of these
commands without using up your turn:

  status - lists food, health, distance traveled, and day.
  help   - lists all the commands.
  quit   - will end the game.
  
You can also use these shortcuts for commands:

  't', 'r', 'h', 's', '?', 'q'
  
"""

good_luck_text = "Good luck, and see you in Oregon!"


# Model -- variables that collectivel represent the state of the game

miles_left = 2000
food_remaining = 500
health_level = 5
month = 3
day = 1
sickness_suffered_this_month = 0
player_name = None

# Constants -- parameters that define the rules of the game,
# but which don't change.
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7

MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
HEALTH_CHANGE_PER_REST = 1
MAX_HEALTH = 5
MONTH_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Name: is_last_day
# Description: Tells us if this is the last day of the month
# Input: day (int) the number of the day this month, and month (int) the month number
# Returns: boolean, whether this day is the last in the month


def is_last_day_of_month(day, month):
    global MONTH_LENGTH
    if MONTH_LENGTH[month] == day:
        print("This is the last day of the month.")
        return True
    elif MONTH_LENGTH[month] != day:
        print("This is not the last day of the month.")
        return False

# Name: set_sick_days
# Description: sets the sick days this month whenever a new month takes place
# Input: number of sick days in a month (int)


def set_sick_days(monthly_sick_days):
    global MONTH_LENGTH
    sick_list = list(range(1, MONTH_LENGTH[month - 1]))
    while monthly_sick_days >= 1:
        monthly_sick_days -= 1
        return random.choice(sick_list)
# Actions to take when a random sickness occurs.


def handle_sickness():
    # TODO(student): write the code for this function
    print("handle_sickness() not yet implemented!")

# Name: consume_food()
# Description: Updates the model to reflect the fact that one day of food was consumed.

def consume_food():
    global food_remaining
    while food_remaining >= 5:
        food_remaining -= 5

# Name: next_day
# Description: Moves the clock forward a day


def next_day():
    # TODO(student): write the code for this function.
    print("next_day() not yet implemented!")

# Name: advance_game_clock
# Description: Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness.
#
# Input: num_days - an integer number of days that elapse.


def advance_game_clock(num_days):
    # TODO(student): write code for this function
    print("advance_game_clock() not yet implemented!")


# Actions to take when player chooses 'travel' action
def handle_travel():
    # TODO(student): write code for this function
    travel_days = random.choice(
        list(range(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)))
    travel_distance = random.choice(
        list(range(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)))
    print("You moved " + str(travel_distance) +
          " miles in " + str(travel_days) + " days.")

# Actions to take when player chooses 'rest' action


def handle_rest(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL, MAX_HEALTH):
    # TODO(student): write code for this function
    global health_level
    rest_days = random.choice(
        list(range(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)))
    while health_level < MAX_HEALTH:
        health_level += 1
    print("You rested for " + str(rest_days) + " days")
    print("Your health is now " + str(health_level))


# Actions to take when player chooses 'hunt' action
def handle_hunt():
    # TODO(student): write code for this function
    print("handle_hunt() not yet implemented!")


# Actions to take when player chooses 'status' action
def handle_status(miles_left, food_remaining, health_level, month, day, sickness_suffered_this_month):
    print("Miles left: " + str(miles_left))
    print("Health: " + str(health_level))
    print("Month: " + str(month))
    print("Day: " + str(day))
    print("Sicknesses suffered this month: " + str(sickness_suffered_this_month))

# Actions to take when player chooses 'help' action


def handle_help():
    # TODO(student): write code for this function
    print(help_text)

# Actions to take when player chooses 'quit' action


def handle_quit():
    # TODO(student): write code for this function
    print("handle_quit() not yet implemented!")


# Actions to take when player enters an invalid choice.
def handle_invalid_input(response):
    print(str(response) + "is not a valid input. Please choose another action. To see the list of inputs and actions, please enter the help menu by pressing h or typing help.")


# Inspects the model and determines if the game has ended for any reason (e.g.
# player is out of food, or has reached Oregon, or is out of time, or too sick)
#
# Returns: True if game is over, False otherwise.
def game_is_over():
    # TODO(student): write code for this function
    print("game_is_over() not yet implemented!")


# Inspects the model and determines if the player has won.
#
# Returns: True if game is over, False otherwise.
def player_wins():
    # TODO(student): write code for this function
    print("player_wins() not yet implemented!")


# Returns a string with the explanation of why the player has lost.
# If the player hasn't lost, returns an empty string.
def loss_report():
    # TODO(student): write code for this function
    print("loss_report() not yet implemented!")


# The main program. No need to modify anything below here.

print(welcome_text + help_text + good_luck_text)
player_name = input("\nWhat is your name, player?: ")

playing = True
while playing:
    print()
    action = input("Choose an action, {0} -->".format(player_name))
    if action == "travel" or action == "t":
        handle_travel()
    elif action == "rest" or action == "r":
        handle_rest(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST, MAX_HEALTH)
    elif action == "hunt" or action == "h":
        handle_hunt()
    elif action == "quit" or action == "q":
        handle_quit()
    elif action == "help" or action == "?":
        handle_help()
    elif action == "status" or action == "s":
        handle_status(miles_left, food_remaining, health_level,
                      month, day, sickness_suffered_this_month)
    else:
        handle_invalid_input(action)

    if game_is_over():
        playing = False

if player_wins():
    print("\n\nCongratulations you made it to Oregon alive!")
    handle_status()
else:
    print("\n\nAlas! You lose.")
    handle_status()
    print(loss_report())
