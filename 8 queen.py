Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def is_safe(board, row, col):
...     """Checks if a queen can be safely placed at board[row][col]."""
...     # Check this row on left side
...     for i in range(col):
... 
...         if board[row][i] == 1:
...             return False
...         
... 
...     # Check upper diagonal on left side
...     for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
...         if board[i][j] == 1:
...             return False
... 
...     # Check lower diagonal on left side
...     for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
...         if board[i][j] == 1:
...             return False
... 
...     return True
... 
... def solve_n_queens_util(board, col):
...     """Utility backtracking function to solve N-Queens."""
...     if col >= len(board):
...         return True
... 
...     for i in range(len(board)):
...         if is_safe(board, i, col):
...             board[i][col] = 1 # Place queen
...             
...             if solve_n_queens_util(board, col + 1):
...                 return True
...                 
...             board[i][col] = 0 # Backtrack
...             
...     return False
... 
... def solve_8_queens():
...     n = 8
...     board = [[0] * n for _ in range(n)]
...     
...     if not solve_n_queens_util(board, 0):
...         print("Solution does not exist")
...         return False
...         
    print("8-Queens Matrix Solution:")
    for row in board:
        print(" ".join(map(str, row)))
    return True

