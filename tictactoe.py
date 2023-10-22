# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Tic Tac Toe Game

# Initialize the game board
board = [" " for _ in range(9)]

# Function to display the game board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_win(player, board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to play the game
def play_game():
    current_player = "X"
    is_game_over = False

    while not is_game_over:
        display_board(board)
        position = int(input(f"Player {current_player}, choose your position from 1 to 9 : ")) - 1

        if board[position] == " ":
            board[position] = current_player

            if check_win(current_player, board):
                display_board(board)
                print(f"Player {current_player} wins!the game yay!!!")
                is_game_over = True
            elif " " not in board:
                display_board(board)
                print("It's a tie!!!!haha")
                is_game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Position already taken!!!. Try again!!!!.")

# Start the game
play_game()
