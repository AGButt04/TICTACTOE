import copy
import math

class TicTacToeAI:
    def __init__(self):
        self.X = "X"
        self.O = "O"
        self.EMPTY = None

    def initial_state(self):
        """
        Returns starting state of the board.
        """
        pass

    def get_best_move(self, board):
        """
        Main interface method - converts board and returns the best move.
        """

    def player(self, board):
        """
        Returns the player who has the next turn on a board.
        """
        pass


    def actions(self, board):
        """
        Returns all the possible actions (i, j) that the current player can take.
        """
        pass

    def result(self, board, action):
        """
        Returns the board that results from making a action (i, j) on the board.
        """
        pass

    def winner(self, board):
        """
        Returns the winner of the game, if there is one.
        """
        pass

    def terminal(self, board):
        """
        Returns True if the game is over, False otherwise.
        """
        pass

    def utility(self, board):
        """
        Returns 1 if X won the game, -1 for O, 0 otherwise.
        """
        pass

    def minimax(self, board):
        """
        Returns the optimal action for the current player on the board.
        """
        pass

    def minimax_value(self, board):
        """
        Helper function for minimax to get the utility value of the current player.
        """
        pass