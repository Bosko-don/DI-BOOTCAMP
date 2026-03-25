# ============================================================
# TIC TAC TOE GAME IN PYTHON
# Topics: Lists, Loops, Conditionals, Functions, User Input
# ============================================================

def display_board(board):
    """
    Display the current state of the game board.
    board is a 2D list (3x3 grid).
    """
    print("\n" + "=" * 13)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * 13)
    print("=" * 13 + "\n")


def player_input(board, player):
    """
    Get and validate player's move.
    Returns tuple (row, col) if valid, None if invalid.
    """
    while True:
        try:
            print(f"Player {player}'s turn")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            # Check if input is within valid range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("❌ Invalid input! Row and column must be between 0 and 2.")
                continue
            
            # Check if cell is empty
            if board[row][col] != " ":
                print("❌ That cell is already taken! Choose another one.")
                continue
            
            return (row, col)
            
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


def check_win(board, player):
    """
    Check if the current player has won.
    Returns True if player has 3 in a row, False otherwise.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Check diagonals
    # Top-left to bottom-right
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    # Top-right to bottom-left
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False


def check_tie(board):
    """
    Check if the game is a tie (all cells filled, no winner).
    Returns True if tie, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # Found empty cell, not a tie
    return True  # No empty cells found


def switch_player(current_player):
    """
    Switch between players X and O.
    """
    return "O" if current_player == "X" else "X"


def play():
    """
    Main game loop - manages the flow of the game.
    """
    # Step 1: Initialize the game board (3x3 grid with empty spaces)
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    current_player = "X"  # X goes first
    game_active = True
    winner = None
    
    print("=" * 40)
    print("🎮 WELCOME TO TIC TAC TOE! 🎮")
    print("=" * 40)
    print("Players take turns placing X or O on the grid.")
    print("First to get 3 in a row wins!")
    print("Enter row and column numbers (0-2) to make your move.\n")
    
    # Step 6: Main game loop
    while game_active:
        # Display the board
        display_board(board)
        
        # Get player input
        move = player_input(board, current_player)
        if move is None:
            continue
        
        row, col = move
        
        # Update the board with player's move
        board[row][col] = current_player
        
        # Check for winner
        if check_win(board, current_player):
            display_board(board)
            winner = current_player
            game_active = False
        
        # Check for tie
        elif check_tie(board):
            display_board(board)
            game_active = False
        
        # Switch player if game continues
        else:
            current_player = switch_player(current_player)
    
    # Display final result
    print("=" * 40)
    if winner:
        print(f"🏆 PLAYER {winner} WINS! 🏆")
    else:
        print("🤝 IT'S A TIE! 🤝")
    print("=" * 40)
    
    # Ask to play again
    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == 'y':
        play()
    else:
        print("Thanks for playing! Goodbye! 👋")


# Start the game
if __name__ == "__main__":
    play()
