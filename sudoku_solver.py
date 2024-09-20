def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False

    # Check the column
    if num in (grid[i][col] for i in range(9)):
        return False

    # Check the 3x3 box
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + box_row_start][j + box_col_start] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num  # Place the number

            if solve_sudoku(grid):
                return True  # If solved, return true

            grid[row][col] = 0  # Reset (backtrack)

    return False  # Trigger backtracking

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku Grid:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
