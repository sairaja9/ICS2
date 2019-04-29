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

# Tries to interpret a string as an integer, returns the result.
# returns a default value if the interpretation fails.
def safe_to_integer(value, default=0):
  try:
    return int(value)
  except (ValueError, TypeError):
    return default
    
# Prompts user for an integer input that must be in some range.
# Keeps asking for a valid value until the user provides one in that range.
# Returns: user-supplied integer. Guaranteed to be within range.
def get_valid_integer(prompt, min_value, max_value):
	valid = False
	while not valid:
		value = safe_to_integer(input(prompt + "--> "))
		if value < min_value or value >= max_value:
			print("Enter a value from {0} to {1}. Try again.".format(
			    min_value, max_value - 1))
		else:
			valid = True
	return value

# Sets a flag to quit the next time through the main loop.
def handle_quit():
  global running
  running = False

# Prompts the user for the location of the item to view, 
# then prints it.
#
# TODO: Student must implement this.
def handle_view_item():
  item_list = input("which list is your item in?: ")
  item = input("Which item are you looking for?: ")

# Prompts the user to specify a list, then prints all items
# in that list.
def handle_view_list():
  print('handle_view_list() not implemented yet. Student: this is your task.')

# Prompts the user for a list, item index, and new item value,
# then sets the item in the specified position to the new value.  
def handle_update_item():
  print('handle_update_item() not implemented yet. Student: this is your task.')

# Gives user feedback about bad input, offers help.
def handle_invalid_input(value):
  print('Sorry, "' + value +'" is not a valid input.')
  print('Type "help" if you need help')

# Offers help.
def handle_help():
  print(help_text)

shopping_cart = [
  ['tooth paste', 'q-tips', 'milk'],
  ['milk', 'candy', 'apples'],
  ['planner', 'pencils', 'q-tips']
]

## Main program
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
  else: 
    handle_invalid_input(action)