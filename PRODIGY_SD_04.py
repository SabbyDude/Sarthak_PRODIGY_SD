import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    UNASSIGNED = 0
    N = 9

    def solve_sudoku(self, board):
        row_col = self.find_unassigned_location(board)
        if row_col is None:
            return True

        row, col = row_col

        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = num
                if self.solve_sudoku(board):
                    return True
                board[row][col] = self.UNASSIGNED
        return False

    def find_unassigned_location(self, board):
        for row in range(self.N):
            for col in range(self.N):
                if board[row][col] == self.UNASSIGNED:
                    return (row, col)
        return None

    def is_safe(self, board, row, col, num):
        for x in range(self.N):
            if board[row][x] == num or board[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

class SudokuGUI:
    def __init__(self, root):
        self.solver = SudokuSolver()
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(grid_frame, width=2, font=('Arial', 18), justify='center', borderwidth=2, relief='solid')
                self.cells[row][col].grid(row=row, column=col, padx=5, pady=5)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve, font=('Arial', 18))
        solve_button.pack(pady=20)

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                cell_value = self.cells[row][col].get()
                if cell_value.isdigit():
                    current_row.append(int(cell_value))
                else:
                    current_row.append(0)
            board.append(current_row)
        return board

    def set_board(self, board):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                if board[row][col] != 0:
                    self.cells[row][col].insert(0, str(board[row][col]))

    def solve(self):
        board = self.get_board()
        if self.solver.solve_sudoku(board):
            self.set_board(board)
        else:
            messagebox.showerror("Error", "No solution exists")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
