#this is code for tic tac tow game in python by using tkinter libarary by tejas agrawal 

import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set window title
        self.title("Tic-Tac-Toe")
        # Initialize the game board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Start with player 'X'
        self.current_player = 'X'
        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create buttons for the game board
        self.buttons = [[tk.Button(self, text=' ', font=('Arial', 20), width=6, height=3,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                         for col in range(3)] for row in range(3)]
        # Place buttons on the grid
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col, sticky='nsew')

    def make_move(self, row, col):
        # Check if the selected cell is empty
        if self.board[row][col] == ' ':
            # Update the board with the current player's mark
            self.board[row][col] = self.current_player
            # Update the button text
            self.buttons[row][col].config(text=self.current_player)
            # Check for a winner
            if self.check_winner(row, col):
                # Display winner message
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                # Reset the board
                self.reset_board()
            # Check for a draw
            elif self.check_draw():
                # Display draw message
                messagebox.showinfo("Draw!", "It's a draw!")
                # Reset the board
                self.reset_board()
            else:
                # Switch players
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        player = self.current_player
        # Check row
        if all(self.board[row][c] == player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == player for r in range(3)):
            return True
        # Check diagonal
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        # Check anti-diagonal
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        # Check if all cells are filled
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def reset_board(self):
        # Reset the game board and buttons
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ' '
                self.buttons[row][col].config(text=' ')
        # Reset player turn
        self.current_player = 'X'

if __name__ == "__main__":
    # Create and run the game
    app = TicTacToe()
    app.mainloop()
