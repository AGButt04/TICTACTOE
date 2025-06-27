import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = None
        self.score_label = None
        self.turn = "X"
        self.buttons = []
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
        self.game_over = False
        self.build_window()

    def build_window(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.score_label = tk.Label(self.window, text="Score: X:0 O:0 Ties:0")
        self.score_label.pack(pady = 10)

        button_frame = tk.Frame(self.window)
        button_frame.pack()
        for i in range(9):
            button = tk.Button(button_frame, text=" ", font=("Arial", 30), width=6, height=2, fg="orange",
                                          command=lambda b=None, idx=i: self.button_clicked(idx))
            if i % 2 == 0:
                button.config(bg="#3498db")
            else:
                button.config(bg="#2c3e50")

            row = i // 3
            column = i % 3
            button.grid(row=row, column=column, padx=5, pady=5)
            self.buttons.append(button)

        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.mainloop()

    def button_clicked(self, button_index):
        if self.game_over:
            return
        button = self.buttons[button_index]
        if button["text"] == " ":
            button.config(text=self.turn)
            if self.turn == "X":
                button.config(fg="#e74c3c")  # Red X
                self.turn = "O"
            else:
                button.config(fg="#27ae60")  # Green X
                self.turn = "X"
        self.check_winner()

    def check_winner(self):
        board = [button['text'] for button in self.buttons]
        wins = [[0,1,2], [3,4,5], [6,7,8],
                [0,3,6], [1,4,7], [2,5,8],
                [0,4,8], [2,4,6]]

        for combo in wins:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
                winner = board[combo[0]]
                self.game_over_message(winner)
                self.new_game()
                return

        if " " not in board:
            self.ties += 1
            self.update_score_display()
            messagebox.showinfo("Game over", "Game tied!")
            self.new_game()

    def game_over_message(self, result):
        self.game_over = True
        if result == "X":
            self.x_wins += 1
        else:
            self.o_wins += 1
        messagebox.showinfo("Game Over", f"Player {result} wins!")
        self.update_score_display()

    def update_score_display(self):
        self.score_label.config(text=f"Score: X: {self.x_wins} O: {self.o_wins} Ties: {self.ties}")

    def new_game(self):
        self.game_over = False
        self.turn = "X"
        for button in self.buttons:
            button.config(text=" ")


# Run the game
if __name__ == "__main__":
    TicTacToe()