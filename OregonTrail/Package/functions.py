import random
import variables
import text

# Name: is_last_day
# Description: Tells us if this is the last day of the variables.month
# Input: day (int) the number of the day this variables.month, and variables.month (int) the variables.month number
# Returns: boolean, whether this day is the last in the variables.month

def is_last_day_of_month():
    if variables.MONTH_LENGTH[variables.month - 1] == variables.day:
        return True
    elif variables.MONTH_LENGTH[variables.month - 1] != variables.day:
        return False

# Name: set_sick_days
# Description: sets the sick days this variables.month whenever a new variables.month takes place
# Input: number of sick days in a variables.month (int)

def set_sick_days():
    sick_list = list(range(1, variables.MONTH_LENGTH[variables.month - 1]))
    sick1 = random.choice(sick_list)
    new_sick_list = sick_list.remove(sick1)
    sick2 = random.choice(new_sick_list)
    return sick1, sick2

def handle_sickness():
    if variables.day == set_sick_days():
        print("You fell sick!")
        variables.health_level -= 1
        print("You health has gone down by 1.  Your new health is " + variables.health_level)
    else:
        print("You are in fine condition.")

# Name: consume_food()
# Description: Updates the model to reflect the fact that one day of food was consumed.

def consume_food():
    if variables.food_remaining >= 5:
        variables.food_remaining -= 5

# Name: next_day
# Description: Moves the clock forward a day

def next_day():
    if is_last_day_of_month():
        variables.month += 1
        variables.day = 1
        if variables.month > 12:
            variables.month -= 12
    else:
        variables.day += 1
    consume_food()
    handle_sickness()

# Name: advance_game_clock
# Description: Causes a certain number of days to elapse. The days pass one at a time, and each
# day brings with it a random chance of sickness.
#
# Input: num_days - an integer number of days that elapse.

def advance_game_clock(cycle):
    while cycle > 0:
        next_day()
        cycle -= 1

###################### Action Functions

def handle_travel():
    travel_days = random.choice(list(range(variables.MIN_DAYS_PER_TRAVEL, variables.MAX_DAYS_PER_TRAVEL)))
    travel_distance = random.choice(list(range(variables.MIN_MILES_PER_TRAVEL, variables.MAX_MILES_PER_TRAVEL)))
    print("You moved " + str(travel_distance) + " miles in " + str(travel_days) + " days.")
    ##variables.day += variables.travel_days
    variables.miles_left -= travel_distance
    advance_game_clock(travel_days)

def handle_rest():
    rest_days = random.choice(list(range(variables.MIN_DAYS_PER_REST, variables.MAX_DAYS_PER_REST)))
    while variables.health_level < variables.MAX_HEALTH:
        variables.health_level += 1
    print("You rested for " + str(rest_days) + " days")
    print("Your health is now " + str(variables.health_level))
    advance_game_clock(rest_days)

def handle_hunt():
    variables.food_remaining += 100
    hunt_days = random.choice(list(range(variables.MIN_DAYS_PER_REST, variables.MAX_DAYS_PER_REST)))
    print("You hunted for " + str(hunt_days) + " days and gained 100 pounds of food.")
    advance_game_clock(hunt_days)

################### Non-action functions

def handle_status():
    print("Miles left: " + str(variables.miles_left))
    print("Health: " + str(variables.health_level))
    print("Food remaining: " + str(variables.food_remaining) + " pounds")
    print("Month: " + str(variables.month))
    print("Day: " + str(variables.day))
    print("Sicknesses suffered this month: " + str(variables.sickness_suffered_this_month))

def handle_help():
    print(text.help_text)

def handle_invalid_input(response):
    print(str(response) + "is not a valid input. Please choose another action. To see the list of inputs and actions, please enter the help menu by pressing h or typing help.")


################### Ending functions

def handle_quit():
    return True

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