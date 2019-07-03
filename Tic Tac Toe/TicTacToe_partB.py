import TicTacToe_partA as A
########################################################################################################################################################################################
'''
________________________________________ Part 1 ____________________________________________
'''
########################################################################################################################################################################################


############## Checks for Full Board ################
def is_board_full(board):
  for lists in board:
    for item in lists:
      if item == " ":
        return False
  return True
#####################################################


############### Checks for Valid Move ###############
def is_valid_move(board, location):
  # Check if location is in range
  if location not in range(1, 10):
    return False

  row = (location - 1) // len(board)
  col = (location - 1) % len(board[row])

  if board[row][col] == " ":
    return True
  else:
    return False
######################################################


############### Checks for a Winning Move ############
def winning_move(board):
	# Check for horizontals
	for row in range(0, 3):
		if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
			return True
			
	# Check for verticals
    for col in range(0,3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] != " ":return True
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != " ":return True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != " ":return True
#####################################################
############### END logic functions  #################
