import random
import variables
import text

def test():
  print("Test")
# Name: is_last_day
# Description: Tells us if this is the last day of the variables.month
# Input: day (int) the number of the day this variables.month, and variables.month (int) the variables.month number
# Returns: boolean, whether this day is the last in the variables.month


def is_last_day_of_month():
    if variables.month_LENGTH[variables.month] == variables.day:
        print("This is the last day of the month.")
        return True
    elif variables.month_LENGTH[variables.month] != variables.day:
        print("This is not the last day of the month.")
        return False

# Name: set_sick_days
# Description: sets the sick days this variables.month whenever a new variables.month takes place
# Input: number of sick days in a variables.month (int)


def set_sick_days():
    sick_list = list(range(1, variables.month_LENGTH[variables.month - 1]))
    while variables.monthly_sick_days >= 1:
        variables.monthly_sick_days -= 1
        return random.choice(sick_list)
# Actions to take when a random sickness occurs.


def handle_sickness():
    # TODO(student): write the code for this function
    print("handle_sickness() not yet implemented!")

# Name: consume_food()
# Description: Updates the model to reflect the fact that one day of food was consumed.

def consume_food():
    while variables.food_remaining >= 5:
        variables.food_remaining -= 5

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
    if is_last_day_of_month():
        variables.month += 1
        variables.day = 1
        variables.day += 1
    else:
        variables.day += 1


# Actions to take when player chooses 'travel' action
def handle_travel():
    variables.travel_days = random.choice(list(range(variables.MIN_DAYS_PER_TRAVEL, variables.MAX_DAYS_PER_TRAVEL)))
    variables.travel_distance = random.choice(list(range(variables.MIN_MILES_PER_TRAVEL, variables.MAX_MILES_PER_TRAVEL)))
    print("You moved " + str(variables.travel_distance) + " miles in " + str(variables.travel_days) + " days.")
    variables.day += variables.travel_days

# Actions to take when player chooses 'rest' action


def handle_rest():
    # TODO(student): write code for this function
    variables.rest_days = random.choice(
        list(range(variables.MIN_DAYS_PER_TRAVEL, variables.MAX_DAYS_PER_TRAVEL)))
    while variables.health_level < variables.MAX_HEALTH:
        variables.health_level += 1
    print("You rested for " + str(variables.rest_days) + " days")
    print("Your health is now " + str(variables.health_level))


# Actions to take when player chooses 'hunt' action
def handle_hunt():
    variables.food_remaining += 100
    variables.travel_days = random.choice(list(range(variables.MIN_DAYS_PER_REST, variables.MAX_DAYS_PER_REST)))
    print("You hunted for " + str(variables.travel_days) + " days and gained 100 pounds of food.")

# Actions to take when player chooses 'status' action
def handle_status():
    print("Miles left: " + str(variables.miles_left))
    print("Health: " + str(variables.health_level))
    print("Food remaining: " + str(variables.food_remaining) + " pounds")
    print("Month: " + str(variables.month))
    print("Day: " + str(variables.day))
    print("Sicknesses suffered this month: " + str(variables.sickness_suffered_this_month))

# Actions to take when player chooses 'help' action


def handle_help():
    print(text.help_text)

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