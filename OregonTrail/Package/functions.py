import random
import variables
import text

########## Automatic non-user functions ##########

# Name: is_last_day_of_month
# Description: Tells us if this is the last day of the month
# none
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
    variables.sickness_suffered_this_month = "days " + str(sick_days[0]) + " and " + str(sick_days[1])
    return sick_days

sick_days_this_month = set_sick_days()

def handle_sickness(days_sick):
    if variables.day in days_sick:
        print("You fell sick!")
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
    else:
        variables.day += 1
    consume_food()
    handle_sickness(sick_days_this_month)

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
    print("Sicknesses suffered this month: " +
          str(variables.sickness_suffered_this_month))

def handle_help():
    print(text.help_text)

def handle_invalid_input(response):
    print(str(response) + " is not a valid input. Please choose another action. To see the list of inputs and actions, please enter the help menu by pressing ? or typing help.")


########## Ending Functions ##########

def handle_quit():
    game_is_over()
    return True

# Returns: True if game is over, False otherwise.
def game_is_over():
    return True

# Inspects the model and determines if the player has won.
# Returns: none
def player_wins():
    if variables.health_level > 0 and variables.food_remaining > 0:
        if variables.month < 12 and variables.miles_left == 0:
            print("You won! Congratulations.  You ahve reached Oregon!")
            game_is_over()

# Inspects the model and determines if the game has ended for any reason (e.g.
# player is out of food, or has reached Oregon, or is out of time, or too sick)
# Returns a string with the explanation of why the player has lost.
# If the player hasn't lost, returns an empty string.
def loss_report():
    if handle_quit():
        print("You lost becasue you quit!")
    elif variables.health_level <= 0:
        print("You died due to low health.")
    elif variables.food_remaining <= 0:
        print("You died of starvation.")
    elif variables.month == 1:
        print("You lost.  You did not reach Oregon on time.")
    game_is_over()