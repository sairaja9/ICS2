import random
import variables
import text

########## Automatic non-user functions ##########

# Name: is_last_day_of_month
# Description: Tells us if this is the last day of the month
# Input: none
# Returns: boolean, whether this day is the last in the month (True or False)
def is_last_day_of_month():
    if variables.MONTH_LENGTH[variables.month - 1] == variables.day:
        return True
    elif variables.MONTH_LENGTH[variables.month - 1] != variables.day:
        return False

# Name: set_sick_days
# Description: sets the sick days this month whenever a new month takes place
# Input: none
def set_sick_days():
    sick_days = [random.randint(1, variables.MONTH_LENGTH[variables.month - 1]), random.randint(1, variables.MONTH_LENGTH[variables.month - 1])]
    while sick_days[0] == sick_days[1]:
        sick_days[1] = [random.randint(1, variables.MONTH_LENGTH[variables.month - 1])]
    variables.days_sick = sick_days

def month_one():
    if variables.month == 3:
        set_sick_days()

month_one()

def handle_sickness():
    if variables.day in variables.days_sick:
        print("You fell sick!")
        if variables.health_level >= 0:
            variables.health_level -= 1
        print("Your new health is " + str(variables.health_level))

# Name: consume_food()
# Description: Updates the model to reflect the fact that one day of food was consumed.
def consume_food():
    if variables.food_remaining >= 5:
        variables.food_remaining -= 5


########## Timeline Functions ##########

# Name: next_day
# Description: Moves the clock forward a day
def next_day():
    if is_last_day_of_month():
        variables.month += 1
        variables.day = 1
        if variables.month > 12:
            variables.month -= 12
            variables.day = 1
        set_sick_days()
    else:
        variables.day += 1
    consume_food()
    handle_sickness()

# Name: advance_game_clock
# Description: Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness.
# Input: cycle - an integer number of days that elapse.
def advance_game_clock(cycle):
    while cycle > 0:
        next_day()
        cycle -= 1


########## Action User Functions ##########

def handle_travel():
    travel_days = random.choice(
        list(range(variables.MIN_DAYS_PER_TRAVEL, variables.MAX_DAYS_PER_TRAVEL)))
    travel_distance = random.choice(
        list(range(variables.MIN_MILES_PER_TRAVEL, variables.MAX_MILES_PER_TRAVEL)))
    print("You moved " + str(travel_distance) +
          " miles in " + str(travel_days) + " days.")
    ##variables.day += variables.travel_days
    variables.miles_left -= travel_distance
    advance_game_clock(travel_days)

def handle_rest():
    rest_days = random.choice(
        list(range(variables.MIN_DAYS_PER_REST, variables.MAX_DAYS_PER_REST)))
    while variables.health_level < variables.MAX_HEALTH:
        variables.health_level += 1
    print("You rested for " + str(rest_days) + " days")
    print("Your health is now " + str(variables.health_level))
    advance_game_clock(rest_days)

def handle_hunt():
    variables.food_remaining += 100
    hunt_days = random.choice(list(range(variables.MIN_DAYS_PER_REST, variables.MAX_DAYS_PER_REST)))
    print("You hunted for " + str(hunt_days) +" days and gained 100 pounds of food.")
    advance_game_clock(hunt_days)


########## Non-action User Functions ##########

def handle_status():
    print("Miles left: " + str(variables.miles_left))
    print("Health: " + str(variables.health_level))
    print("Food remaining: " + str(variables.food_remaining) + " pounds")
    print("Month: " + str(variables.month))
    print("Day: " + str(variables.day))
    print("Sick days this month " + str(variables.days_sick))

def handle_help():
    print(text.help_text)

def handle_invalid_input(response):
    print(str(response) + " is not a valid input. Please choose another action. To see the list of inputs and actions, please enter the help menu by pressing ? or typing help.")


########## Ending Functions ##########

def handle_quit():
    playing = False
    return playing

# Inspects the model and determines if the game has ended for any reason (e.g.
# player is out of food, or has reached Oregon, or is out of time, or too sick)
# Returns: True if game is over, False otherwise.
def game_is_over():
    if variables.food_remaining <= 0 or variables.month == 1 or variables.health_level <= 0:
        return True
    elif (variables.health_level > 0 and variables.food_remaining > 0) and (variables.month <= 12 and variables.miles_left <= 0):
        return True
    else:
        return False

# Inspects the model and determines if the player has won.
# Returns: True if ganme is over, False otherwise.
def player_wins():
    if (variables.health_level > 0 and variables.food_remaining > 0) and (variables.month <= 12 and variables.miles_left <= 0):
        return True
    else:
        return False

# Returns a string with the explanation of why the player has lost.
# If the player hasn't lost, returns an empty string.
def loss_report():
    if variables.health_level <= 0:
        print("You died due to low health.")
    elif variables.food_remaining <= 0:
        print("You died of starvation.")
    elif variables.month == 1:
        print("You lost.  You did not reach Oregon on time.")
    else:
        return " "