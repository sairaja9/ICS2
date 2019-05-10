# END logic functions

# N - print_board
# P - print the board with the current state of X, O, and blanks
# I - board: the 3x3 gameboard with the current state
# R - None
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

# Main game loop
player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")
current_player = player1
game_over = False
def convert_to_board_index(board, choose_spot, current_player):
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

# The board starts empty
while not game_over:
    # 1. Ask the user (by name) to select a position on the board
    choose_spot = input("\n{}, please choose a location to place your X: ".format(current_player))

    # 2. Check if the position is valid (not already marked) and update the board.
    #    If it's not valid, ask the user again until they give you a valid position.
    if is_valid_move(board, choose_spot) == True:
        convert_to_board_index(board, choose_spot, current_player)

    # 3. Print the current board
    print(board)
    print_board(board)

    # 4. Check if the player won the game
    #        Print which player won

    # 5. Check if the game is a tie
    #        Print that it is a tie
    #        For extra credit, check if there are no more possible moves to win the game and print that the game is ending early if so.

    # 6. If there's a winner or tie
    #        End the game
    #        Ask if the user wants to play again
    #            If yes, clear the board
    #            If no, game_over = True

    # 7. Switch the players
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

# END main while loop
print("Thanks for playing!")
