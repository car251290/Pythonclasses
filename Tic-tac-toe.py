# Tic-Tac-Toe Game in Python
# Two-player console version

# Initialize board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a tie
def check_tie():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player

        # Check for win or tie
        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()