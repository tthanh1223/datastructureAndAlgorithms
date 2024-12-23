# the N-queen problem involves placing N queens on an NxN chessboard such that no two
# queen attack each other. Queens can attack in the same row, column or diagonals.
# A brute force backtracking approach systematically explores all possible placements and backtracks when a conflict arises.

# Step to Solve:
# 1. Place queens one by one in different rows
# 2. For each row, try placing the queen in all columns:
#       - Check if the placement is valid (no queen in the same column, main diagonal, or anti-diagonal).
# 3. If a valid position is found for all N queens, store the solution
# 4. Backtrack and try other placements until all possibilities are exhausted.

def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        # Check main diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False
        # Check anti-diagonal
        for i,j in zip(range(row - 1, -1 , -1), range(col+1, n)):
            if board[i] == j:
                return False
        return True
    def backtrack(board, row):
        if row == n:
            # Found a valid configuration
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
            # Backtrack
            board[row] = -1
    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print("".join("Q " if i == row else ". " for i in range(n)))
        print("\n")

n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions: {len(solutions)}")
print_solutions(solutions)
