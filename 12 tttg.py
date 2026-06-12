import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(b, player):
    win_states = [
        [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]], # Rows
        [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]], # Cols
        [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]                             # Diagonals
    ]
    return [player, player, player] in win_states

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    for turn in range(9):
        player = 'X' if turn % 2 == 0 else 'O'
        if player == 'X':
            # Human move
            row, col = map(int, input("Enter row and col (0-2) separated by space: ").split())
            while board[row][col] != " ":
                row, col = map(int, input("Cell occupied! Re-enter (0-2): ").split())
            board[row][col] = 'X'
        else:
            # Simple AI move
            empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
            r, c = random.choice(empty_cells)
            board[r][c] = 'O'
            print(f"AI placed 'O' at ({r}, {c})")
            
        print_board(board)
        if check_winner(board, player):
            print(f"Player {player} wins!")
            return
    print("It's a draw!")

# Uncomment to play in a local terminal execution environment
# play_game()
