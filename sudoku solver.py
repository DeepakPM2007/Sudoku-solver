import numpy as np

def print_grid(grid):
    """Prints the Sudoku grid in a visually appealing format"""
    print("\n+-------+-------+-------+")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("+-------+-------+-------+")
        row_str = "| "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += f"{grid[i][j] if grid[i][j] != 0 else '.'} "
        row_str += "|"
        print(row_str)
    print("+-------+-------+-------+\n")

def input_grid():
    """Allows user to input the Sudoku grid"""
    print("Enter your Sudoku puzzle (use 0 for empty cells):")
    print("Separate numbers with spaces, or press enter for an empty row")
    grid = []
    for i in range(9):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            if not row_input:  # If empty input, make empty row
                grid.append([0]*9)
                break
            numbers = row_input.split()
            if len(numbers) != 9:
                print("Please enter exactly 9 numbers (0-9) separated by spaces")
                continue
            try:
                row = [int(num) if 0 <= int(num) <= 9 else 0 for num in numbers]
                grid.append(row)
                break
            except ValueError:
                print("Please enter numbers only (0-9)")
    return grid

def possible(grid, row, column, number):
    """Checks if a number can be placed in a specific position"""
    # Check row
    if number in grid[row]:
        return False

    # Check column
    if number in [grid[i][column] for i in range(9)]:
        return False
    
    # Check 3x3 square
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve(grid, show_all=False):
    """Solves the Sudoku puzzle using backtracking"""
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(grid, row, column, number):
                        grid[row][column] = number
                        solve(grid, show_all)
                        grid[row][column] = 0
                return
    
    # Found a solution
    print_grid(grid)
    if show_all:
        input("Press Enter to see more solutions (if any exist)...")
    else:
        exit()

def main():
    print("SUDOKU SOLVER")
    print("1. Use default puzzle")
    print("2. Enter custom puzzle")
    choice = input("Choose option (1/2): ")
    
    if choice == "1":
        grid = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,0,1,9,0,0,5],
            [0,0,0,0,0,0,0,0,0]
        ]
    else:
        grid = input_grid()
    
    print("\nInput puzzle:")
    print_grid(grid)
    
    show_all = input("Show all possible solutions? (y/n): ").lower() == 'y'
    print("\nSolving...\n")
    
    try:
        solve(grid, show_all)
        if not show_all:
            print("No more solutions found.")
    except KeyboardInterrupt:
        print("\nSolution search stopped by user.")

if __name__ == "__main__":
    main()
