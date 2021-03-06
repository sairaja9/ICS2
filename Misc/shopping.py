shopping_cart = [
    ['tooth paste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
]

welcome_text = '''
Welcome to the shopping cart program. You can maintain several independent
shopping lists all in one place.
'''

help_text = '''
You can take the following actions:

  view item    - prints a single item from a single list in your cart.
  view list    - prints all the items on a single list in your cart.
  update item  - changes the value of a single item on a single list.
  help         - prints instructions for using this program.
  quit         - exits the shopping cart program.

You can also use these shortcuts for commands:

  'vi', 'vl', 'ui', 'h', 'q'

'''

# Sets a flag to quit the next time through the main loop.
def handle_quit():
    global running
    running = False

# Prompts the user for the location of the item to view,
# then prints it.
def handle_view_item():
    global shopping_cart
    list_number = int(input("Which list (number) is your item in?: "))
    item_number = int(input('Which item number are you looking for?: '))
    print(shopping_cart[list_number][item_number])

# Prompts the user to specify a list, then prints all items
# in that list.
def handle_view_list():
    list_number = int(input("Which list would you like to view?: "))
    print(shopping_cart[list_number])

# Prompts the user for a list, item index, and new item value,
# then sets the item in the specified position to the new value.
def handle_update_item():
    global shopping_cart
    list_number = int(input("Which list (number) is your item in?: "))
    item_number = int(input('Which item number are you looking for?: '))
    new_item = input("What would you like to replace " + str(shopping_cart[list_number][item_number]) + " with?: ")
    shopping_cart[list_number].pop(item_number)
    shopping_cart[list_number].insert(item_number, new_item)

# Gives user feedback about bad input, offers help.
def handle_invalid_input(value):
    print('Sorry, "' + value + '" is not a valid input.')
    print('Type "help" if you need help')

# Offers help.
def handle_help():
    print(help_text)

def all_in_one():
    global shopping_cart
    newList = []
    for lists in shopping_cart:
        for item in lists:
            newList.append(item)
    return newList

def count_q_tips(target):
    word = 'q-tips'
    tip_count = 0
    for word in all_in_one():
        if word == target:
            tip_count += 1
    print("There were",tip_count,"q-tips in the list")
    print(all_in_one())

def drink_more_milk():
    for list_index in range (0, len(shopping_cart)):
        if 'milk' not in shopping_cart[list_index]:
            print('Adding "milk" to the list', str(list_index))
            shopping_cart[list_index].append('milk')

def if_you_give_a_mouse_a_cookie():
    for list_index in range (0, len(shopping_cart)):
        if 'milk' in shopping_cart[list_index]:
            print('changing "milk" to milk and cookies in list', str(list_index))
            shopping_cart[list_index].remove('milk')
            shopping_cart[list_index].append('milk and cookies')

def reverse():
    global shopping_cart
    newCart = []
    for lists in shopping_cart:
        reverseCart = []
        newCart.insert(0, reverseCart)
        for item in lists:
            reverseCart.insert(0, item)
    print(newCart)

# Main loop
print(welcome_text)
print(help_text)
running = True
while running:
    print()
    action = input("Choose an action --> ")
    if action == 'view item' or action == 'vi':
        handle_view_item()
    elif action == 'view list' or action == 'vl':
        handle_view_list()
    elif action == 'update item' or action == 'ui':
        handle_update_item()
    elif action == 'help' or action == 'h':
        handle_help()
    elif action == 'quit' or action == 'q':
        handle_quit()
    elif action == 'all in one' or action == 'aio':
        all_in_one()
    elif action == 'count q tips' or action == 'cqt':
        count_q_tips('q-tips')
    elif action == 'drink more milk' or action == 'dmm':
        drink_more_milk()
    elif action == 'add cookies' or action == 'ac':
        if_you_give_a_mouse_a_cookie()
    elif action == 'reverse' or action == 'r':
        reverse()
    else:
        handle_invalid_input(action)