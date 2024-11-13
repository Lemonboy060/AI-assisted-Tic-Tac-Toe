import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        # Game State
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Game Interface
        self.create_header()
        self.create_board_frame()
        self.create_board_buttons()
        self.create_control_buttons()
    
    def create_header(self):
        # Header to show the current player's turn
        self.header = tk.Label(self.root, text="Player X's Turn", font=('Arial', 16, 'bold'), fg="white")
        self.header.grid(row=0, column=0, pady=10)

    def create_board_frame(self):
        # Frame for the grid with background color
        self.board_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        self.board_frame.grid(row=1, column=0, padx=10, pady=10)
    
    def create_board_buttons(self):
        # Create a 3x3 grid of buttons within the board frame
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.board_frame, text="", font=('Arial', 24), width=5, height=2,
                    bg="lightblue",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def create_control_buttons(self):
        # Frame for the control buttons
        control_frame = tk.Frame(self.root)
        control_frame.grid(row=2, column=0, pady=10)
        
        # Reset button
        reset_button = tk.Button(control_frame, text="Reset Game", font=('Arial', 14), command=self.reset_board)
        reset_button.pack(side=tk.LEFT, padx=20)

        # Quit button
        quit_button = tk.Button(control_frame, text="Quit", font=('Arial', 14), command=self.root.quit)
        quit_button.pack(side=tk.LEFT, padx=20)

    def make_move(self, row, col):
        # Make a move if the cell is empty
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text=self.current_player,
                fg="black",
                bg="blue" if self.current_player == "X" else "red"
            )
            if self.check_winner(row, col):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                # Switch player and update the header text
                self.current_player = "O" if self.current_player == "X" else "X"
                self.header.config(text=f"Player {self.current_player}'s Turn", fg="white")
    
    def check_winner(self, row, col):
        # Check if the current player has won
        # Check the row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Check the column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Check the main diagonal
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Check the secondary diagonal
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw (all cells are filled and no winner)
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        # Reset the board and the GUI buttons
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg="lightblue")
        # Update header
        self.header.config(text="Player X's Turn", fg="black")

# Initialize the game
root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()
