board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# Copy your logic functions from part A below:
# This file contains the core functions needed to validate moves in the Tic Tac Toe game
# Implement each function and choose "Run Tests" from the drop down menu to see how you did.
# Once you pass all the tests, you can move on to the next part of the project (user interaction).

# For all functions, "board" is assumed to be a nested list representing your Tic Tac Toe board.
# The board should be 3x3 and each spot should have an "X", "O" or " " (single space).


# N - is_board_full
# P - Checks if there are any open spaces on the board
# I - board: a 3x3 representation of the board as a nested list
# R - True if the board is full, False if there is at least one open space
def is_board_full(board):
    for lists in board:
        for item in lists:
            if item == " ":
                return False
    return True

# N - is_valid_move
# P - Checks if a mark can be placed at the location on the board
# I - board: a 3x3 representation of the board as a nested list
#     location: an int (1-9) indicating where the user wants to place a mark
# R - True if the location is open on the board, False if it is already taken.


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

# N - winning_move
# P - Checks if the previous move resulted in the user winning the game
# I - board: a 3x3 representation of the board as a nested list
# R - True if the user now has 3 marks in a row, False if the user does not

# Old code
    '''
  for i in range (0,3):
    if board[i][i + 1] == "X" or  board[i][i + 1] == "O":
      return True
    elif board[i + 1][i] == "X" or board[i + 1][i] == "O":
      return True
    elif board[i + 1][i - 1] == "X" or board[i + 1][i - 1] == "O":
      return True
    elif board[i + 1][i + 1] == "X" or board[i + 1][i + 1] == "O":
      return True
  return False
  '''


def winning_move(board):
                # Check for horizontals
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
            return True

    # Check for verticals
    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] != " ":
            return True

    # Check for diagonals
    # Diagonal top left to bottom right
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != " ":
        return True

    # Diagonal top right to bottom left
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != " ":
        return True

    return False

# Extra Credit: uncomment the following line and implement the function
# N - winning_move_possible
# P - Determines if the game is an inevitable tie or if someone can still win
# I - board: a 3x3 representation of the board as a nested list
# R - True if there's at least one combination of moves that would let a player win, False if the game must tie
# def winning_move_possible(board):


# Write your test code here:
'''
def winning_move_possible():
  #still working on it (temporarily moved on to part B)
'''
