

def is_board_full(board):
    for lists in board:
        for item in lists:
            if item == " ":
                return False
    return True


def is_valid_move(board, location):

    if location not in range(1, 10):
        return False

    row = (location - 1) // len(board)
    col = (location - 1) % len(board[row])

    if board[row][col] == ' ':
        return True
    else:
        return False

    '''
	for i in range (0,3):
		if board[i][i + 1] == "X" or	board[i][i + 1] == "O":
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

    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ":
            return True

    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] != " ":
            return True

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != " ":
        return True

    return False


def convert_to_board_index(board, choose_spot):
    if choose_spot in range(1, 4):
        row = 0
    elif choose_spot in range(4, 7):
        row = 1
    elif choose_spot in range(7, 10):
        row = 2

    if choose_spot == 1 or choose_spot == 4 or choose_spot == 7:
        col = 0
    elif choose_spot == 2 or choose_spot == 5 or choose_spot == 8:
        col = 1
    elif choose_spot == 3 or choose_spot == 6 or choose_spot == 9:
        col = 2

    if current_player == player1:
        board[row][col] = 'X'
    elif current_player == player2:
        board[row][col] = 'O'


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def print_board(board):
    print("\n {} | {} | {}\n---|---|---\n {} | {} | {}\n---|---|---\n {} | {} | {}".format(
        board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]))


welcome_message = """Welcome to Tic Tac Toe!

This game supports two players.
Each player will alternate placing an X or O on the 3x3 grid until one player gets 3 of their mark in a row, column, or diagonal.
If the board fills up without anyone getting 3 in a row, the players will tie.

You will tell the computer where to put your mark by using the numbering system below:

		 1 | 2 | 3 
		---|---|---
		 4 | 5 | 6 
		---|---|---
		 7 | 8 | 9

Good luck!
"""

print(welcome_message)


player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")
current_player = player1
game_over = False


while not game_over:

    choose_spot = int(
        input("\n{}, please choose a location to place your X: ".format(current_player)))

    if is_valid_move(board, choose_spot) == True:
        convert_to_board_index(board, choose_spot)

    print_board(board)

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1


print("Thanks for playing!")