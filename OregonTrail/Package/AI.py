import variables

action_list = ["travel", "rest", "hunt"]

def choose_action():
    if variables.health_level < 3:
        smart_action = action_list[1]
    elif variables.food_remaining < 100:
        smart_action = action_list[2]
    elif variables.health_level < 3 and variables.food_remaining < 100:
        smart_action = action_list[2]
    else:
        smart_action = action_list[0]
    return smart_action