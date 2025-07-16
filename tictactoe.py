import tkinter as tk
from tkinter import messagebox
from minimax_AI import TicTacToeAI
import winsound


class TicTacToe:
    def __init__(self):
        self.status_label = None
        self.window = None
        self.score_label = None
        self.turn = "X"
        self.buttons = []
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
        self.game_over = False
        self.ai = TicTacToeAI()
        self.game_mode = "human_vs_human"
        self.ai_player = "O"
        self.build_window()

    def make_ai_move(self):
        if self.game_over:
            return
        board_2d = self.buttons_to_board()
        ai_move = self.ai.minimax(board_2d)
        if ai_move:
            self.apply_ai_move(ai_move)
            self.turn = "X"
            self.check_winner()
        self.status_label.config(text="")

    def buttons_to_board(self):
        """Convert buttons to board for the AI to understand"""
        board = []
        for i in range(3):
            row = []
            for j in range(3):
                button_index = i * 3 + j
                text = self.buttons[button_index]["text"]
                if text == " ":
                    row.append(None)
                else:
                    row.append(text)
            board.append(row)
        return board

    def apply_ai_move(self, ai_move):
        """Take AI move (row, col) and update the GUI"""
        row, col = ai_move
        button_index = row * 3 + col
        button = self.buttons[button_index]
        button.config(text=self.turn)
        button.config(bg="#27ae60")  # Green for O

    def set_game_mode(self, mode):
        """Set the game mode and reset the game"""
        self.game_mode = mode
        self.play_beep_sound()
        self.new_game()  # Reset board for new mode

    def build_window(self):
        """Build the window"""

        self.window = tk.Tk()
        self.window.title("🎮 Tic-Tac-Toe with AI")
        self.window.configure(bg="#2c3e50")  # Dark background

        # Title
        title_label = tk.Label(self.window, text="🎮 Tic-Tac-Toe",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=(20, 10))

        # Score label with better styling
        self.score_label = tk.Label(self.window,text="Score: X:0 O:0 Ties:0",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.score_label.pack(pady=5)
        self.status_label = tk.Label(
            self.window,
            text="",  # Start empty
            font=("Arial", 14, "italic"),
            bg="#2c3e50",
            fg="#f39c12"  # Orange color
        )
        self.status_label.pack(pady=5)

        # Game mode section with frame styling
        mode_frame = tk.Frame(self.window, bg="#2c3e50")
        mode_frame.pack(pady=10)

        tk.Label(
            mode_frame,text="Choose Game Mode:", font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        ).pack(pady=(0, 10))

        button_frame_mode = tk.Frame(mode_frame, bg="#2c3e50")
        button_frame_mode.pack()

        # Styled mode buttons
        tk.Button(
            button_frame_mode,
            text="👥 Human vs Human",
            command=lambda: self.set_game_mode("human_vs_human"),
            bg="#3498db",
            fg="white",
            font=("Arial", 15, "bold"),
            padx=20,
            pady=10,
            relief="flat",
            activebackground="#2980b9"
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            button_frame_mode,
            text="🤖 Human vs AI",
            command=lambda: self.set_game_mode("human_vs_ai"),
            bg="#e74c3c",
            fg="white",
            font=("Arial", 15, "bold"),
            padx=20,
            pady=10,
            relief="flat",
            activebackground="#c0392b"
        ).pack(side=tk.LEFT, padx=10)

        # Game board with frame
        board_container = tk.Frame(self.window, bg="#2c3e50")
        board_container.pack(pady=10)

        button_frame = tk.Frame(board_container, bg="#34495e", relief="raised", bd=2)
        button_frame.pack(padx=20, pady=20)

        for i in range(9):
            button = tk.Button(
                button_frame,
                text=" ",
                font=("Arial", 28, "bold"),
                width=4,
                height=2,
                fg="orange",
                command=lambda idx=i: self.button_clicked(idx),
                relief="flat",
                bd=2
            )
            if i % 2 == 0:
                button.config(bg="#3498db", activebackground="#2980b9")
            else:
                button.config(bg="#2c3e50", activebackground="#34495e")

            row = i // 3
            column = i % 3
            button.grid(row=row, column=column, padx=3, pady=3)
            self.buttons.append(button)

        self.window.geometry("600x700")
        self.window.resizable(False, False)
        self.window.mainloop()

    def button_clicked(self, button_index):
        if self.game_over:
            return

        button = self.buttons[button_index]
        if button["text"] == " ":
            button.config(text=self.turn)
            if self.turn == "X":
                button.config(bg="#e74c3c")  # Red X
                self.turn = "O"
            else:
                button.config(bg="#27ae60")  # Green O
                self.turn = "X"

            self.check_winner()

            should_ai_play = (not self.game_over and
                              self.game_mode == "human_vs_ai" and
                              self.turn == self.ai_player)

            if should_ai_play:
                self.status_label.config(text="🤖 Computer thinking...")
                self.window.update()
                self.window.after(500, self.make_ai_move)
                self.play_beep_sound()

    def check_winner(self):
        board_2d = self.buttons_to_board()
        winner = self.ai.winner(board_2d)
        if winner:
            # Use your existing logic to find and highlight winning combo
            board = [button['text'] for button in self.buttons]
            wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
            for combo in wins:
                if board[combo[0]] == board[combo[1]] == board[combo[2]] == winner:
                    self.winner_highlight(combo)
                    break
            self.game_over_message(winner)
            self.new_game()
            return

        if " " not in [button["text"] for button in self.buttons]:
            self.ties += 1
            self.update_score_display()
            messagebox.showinfo("Game over", "Game tied!")
            self.new_game()


    def play_win_sound(self):
        winsound.Beep(1000,500)

    def play_beep_sound(self):
        winsound.Beep(500,200)

    def winner_highlight(self, winning_combo):
        for index in winning_combo:
            self.buttons[index].config(bg="red", fg = "white")

    def game_over_message(self, result):
        self.game_over = True
        if result == "X":
            self.x_wins += 1
        else:
            self.o_wins += 1
        self.play_win_sound()
        messagebox.showinfo("Game Over", f"Player {result} wins!")
        self.update_score_display()

    def update_score_display(self):
        self.score_label.config(text=f"Score: X: {self.x_wins} O: {self.o_wins} Ties: {self.ties}")

    def new_game(self):
        self.game_over = False
        self.turn = "X"
        for i, button in enumerate(self.buttons):
            button.config(text=" ")
            if i % 2 == 0:
                button.config(bg="#3498db", activebackground="#2980b9")
            else:
                button.config(bg="#2c3e50", activebackground="#34495e")


# Run the game
if __name__ == "__main__":
    TicTacToe()