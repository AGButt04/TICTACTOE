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
        board = [[self.EMPTY] * 3 for _ in range(3)]
        return board

    def get_best_move(self, board):
        """
        Main interface method - converts board and returns the best move.
        """
        pass

    def player(self, board):
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)
        return self.X if x_count == o_count else self.O

    def actions(self, board):
        """
        Returns all the possible actions (i, j) that the current player can take.
        """
        actions = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == self.EMPTY:
                    actions.add((i,j))

        return actions

    def result(self, board, action):
        if board[action[0]][action[1]] != self.EMPTY:
            raise ValueError("Invalid action")
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = self.player(board)
        return new_board

    def winner(self, board):
        """
        Returns the winner of the game, if there is one.
        """
        winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for combo in winning_combinations:
            first = combo[0]
            second = combo[1]
            third = combo[2]
            if board[first[0]][first[1]] == board[second[0]][second[1]] == board[third[0]][third[1]]\
                and board[first[0]][first[1]] != self.EMPTY:
                    return board[first[0]][first[1]]
        return None

    def terminal(self, board):
        """
        Returns True if the game is over, False otherwise.
        """
        if self.winner(board) is not None:
            return True

        # Check if there's a tied
        for i in range(3):
            for j in range(3):
                if board[i][j] == self.EMPTY:
                    return False
        return True

    def utility(self, board):
        """
        Returns 1 if X won the game, -1 for O, 0 otherwise.
        """
        if self.terminal(board):
            check_winner = self.winner(board)
            if check_winner == self.O:
                    return -1
            elif check_winner == self.X:
                    return 1
            else:
                return 0
        else:
            return None

    def minimax(self, board):
        if self.terminal(board):
            return None

        turn = self.player(board)
        best_action = None

        if turn == self.X:
            best_value = -math.inf
            for action in self.actions(board):
                value = self.minimax_value(self.result(board, action), 0)
                if value > best_value:
                    best_value = value
                    best_action = action
        else:
            best_value = math.inf
            for action in self.actions(board):
                value = self.minimax_value(self.result(board, action), 0)
                if value < best_value:
                    best_value = value
                    best_action = action
        return best_action

    def minimax_value(self, board, depth):
        if self.terminal(board):
            return self.utility(board) * (10 - depth)

        if self.player(board) == self.X:
            best_value = -math.inf
            for action in self.actions(board):
                value = self.minimax_value(self.result(board, action), depth + 1)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = math.inf
            for action in self.actions(board):
                value = self.minimax_value(self.result(board, action), depth + 1)
                best_value = min(best_value, value)
            return best_value


# Test the implementation
if __name__ == "__main__":
    ai = TicTacToeAI()
    board1 = [
        ["X", "X", None],
        ["O", None, None],
        [None, None, None]
    ]
    print("Test 1 - AI as O should block X:")
    print("Current player:", ai.player(board1))  # Should print: O
    print("AI move:", ai.minimax(board1))  # Should print: (0,2)
    print("Expected: (0, 2) to block X diagonal")
    # Simple test cases for TicTacToeAI

    board2 = [
        ["X", "X", None],
        ["O", "O", None],
        [None, None, None]
    ]
    print("Test 1 - AI (O) should block at (0, 2):")
    print("Current player:", ai.player(board2))  # O
    print("AI move:", ai.minimax(board2))  # Expected: (0, 2)
    print()

    board3 = [
        ["X", "O", "X"],
        ["X", "O", "X"],
        [None, None, "O"]
    ]
    print("Test 3 - AI (X) should pick a strategic move (2, 1):")
    print("Current player:", ai.player(board3))  # X
    print("AI move:", ai.minimax(board3))  # Expected: corner or best available
    print()

