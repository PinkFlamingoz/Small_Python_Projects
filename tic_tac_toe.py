# Import
import random
from basic_functions import get_valid_input

# Start and control the game
def main():
    board = [" "] * 10 #---------------------------------------------- Initialize the game board
    print_welcome_message() #----------------------------------------- Print welcome message
    print_board(board) #---------------------------------------------- Print the initial (empty) game board

    # Until the game board is full
    while not is_board_full(board):
        
        # CASE 1: If the computer has won
        if not is_winner(board, "O"):
            board[get_player_move(board)] = "X" #--------------------- Let the player make a move
            print_board(board) 
        else: #------------------------------------------------------- If the computer has won, end the game
            print("\nYou lost to the computer!")
            return
        
        # CASE 2: If the player has won
        if not is_winner(board, "X"):
            move = get_computer_move(board) #------------------------- Let the computer make a move
            if move == 0: #------------------------------------------- If the move is zero (the board is full)
                print("\nTie game!")
            else: #--------------------------------------------------- If the game isn't over, make the move
                board[move] = "O"
                print(f'\nComputer placed an "O" in position {move}.')
                print_board(board)
        else: #------------------------------------------------------- If the player has won, end the game
            print("\nYou won the game!")
            return
        
    # CASE 3: If the board is full and no one has won, it's a tie
    print("\nTie game!")


# Print a welcome message and show the board layout
def print_welcome_message():
    print("Welcome to Tic Tac Toe!")
    print("The board is numbered as follows:")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")


# Print the current state of the board, each cell of the board corresponds to a number from 1 to 9
def print_board(board):
    print("\nCurrent board:")
    print(f" {board[1]} | {board[2]} | {board[3]}") #-- top row
    print("---|---|---")
    print(f" {board[4]} | {board[5]} | {board[6]}") #-- middle row
    print("---|---|---")
    print(f" {board[7]} | {board[8]} | {board[9]}\n") # bottom row


# Check if a certain position on the board is free
# Return True if the board at position pos is free (contains a space ' ').
# Return False otherwise.
def is_space_free(board, pos):
    return board[pos] == " "


# Check if a player has won the game
# Use any() function to check if any winning combination is met.
# If any combination is met, return True.
# If no combination is met, return False.
def is_winner(board, mark):
    # Define all possible winning combinations in a list of tuples
    winning_combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    return any(
        board[a] == board[b] == board[c] == mark for a, b, c in winning_combinations)


# Function to check if the game board is full
# If there's only one or no empty space (' ') on the board, it means the board is full.
# Return True if the board is full, False otherwise.
def is_board_full(board):
    return board.count(" ") <= 1


# Get a valid move from the player
def get_player_move(board):
    while True:
        move = get_valid_input(int, "Please select a position to place an 'X' (1-9): ") # Ask the player for their move
        if int(move) in range(1, 10) and is_space_free(board, int(move)): #-------------- If the input is a digit, is between 1 and 9 (inclusive), and the space on the board is free
            return int(move) #----------------------------------------------------------- Return the move
        print("\nInvalid move. Please try again.") #------------------------------------- If the move was invalid, notify the player and start the loop again


# Decide a move for the computer
# enumerate(board) is a built-in Python function that takes an iterable (like a list) and returns an iterator that produces tuples,
# where the first element of each tuple is the index of the item in the iterable, and the second element is the item itself.
# In this case, it's used on board, so it will produce tuples like (1, 'X'), (2, ' '), (3, 'O'), etc.
# [pos for pos, mark in enumerate(board) if mark == ' ' and pos != 0] is a list comprehension, which is a compact way of creating a list in Python.
# It creates a new list that includes pos (the position on the board) for each position-mark pair in board where the mark is a space (i.e., the position is unoccupied) and the position is not zero.
def get_computer_move(board):
    
    possible_moves = [pos for pos, mark in enumerate(board) if mark == " " and pos != 0]  # List all the empty spaces on the board
    print(f"\nFree spaces on the board: {possible_moves}")
    
    # CASE 1: If there is a winning move, this checks for each x and o if there is a winning move, in such a way it also defends itself
    for mark in ["X", "O"]: #------------------------------------------------------ For each mark 'X' and 'O'        
        for move in possible_moves: #---------------------------------------------- For each possible move            
            board_copy = board.copy() #-------------------------------------------- Copy the board            
            board_copy[move] = mark #---------------------------------------------- Make the move on the copied board
            if is_winner(board_copy, mark): #-------------------------------------- If this move would result in a win
                return move #------------------------------------------------------ Return the move
    
    # CASE 2: If there are no winning moves, try to take a corner space
    corners = [move for move in [1, 3, 7, 9] if move in possible_moves]
    if corners: 
        return random.choice(corners)

    # CASE 3: If no corners are available, try to take the center
    if 5 in possible_moves: 
        return 5
    
    # CASE 4: If neither corners nor center is available, choose a random edge
    return random.choice([move for move in possible_moves if move in [2, 4, 6, 8]])


# Main loop
while True:
    if input("Do you want to play Tic Tac Toe? (Y/N): ").lower() in ["y", "yes"]:
        main()
    else:
        break
