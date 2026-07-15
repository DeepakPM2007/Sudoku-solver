# Sudoku Solver

A simple, interactive Sudoku solver written in Python using the backtracking algorithm. 

## Features
- **Interactive CLI:** Choose to solve a built-in default puzzle or input your own.
- **Custom Puzzle Input:** Enter your puzzle row by row directly in the terminal.
- **Multiple Solutions:** Option to find just the first solution or explore all possible solutions for a given puzzle.
- **Visual Grid:** Prints the Sudoku grid in a clean, visually appealing format.

## Requirements
- Python 3.x
- NumPy (`pip install numpy`)

## Usage
Run the script from your terminal:

```bash
python "sudoku solver.py"
```

You will be prompted to:
1. Use the default built-in puzzle.
2. Enter a custom puzzle (use `0` for empty cells, separate numbers with spaces).
3. Decide whether to show all possible solutions or just the first one.

## How it works
The script uses a standard **backtracking algorithm**. It systematically places numbers (1-9) in empty cells and checks if the placement is valid according to Sudoku rules (checking the row, column, and 3x3 subgrid). If it encounters a dead-end, it backtracks to the previous cell and tries the next possible number.
