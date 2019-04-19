# Model -- variables that collectively represent the state of the game
miles_left = 2000
food_remaining = 500
health_level = 5
month = 3
day = 1
sickness_suffered_this_month = 0
player_name = None
days_sick = []

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