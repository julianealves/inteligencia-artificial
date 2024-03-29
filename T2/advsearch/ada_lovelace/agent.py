from typing import Tuple
from advsearch.othello.board import Board
import numpy as np
from copy import deepcopy


def make_move(the_board: Board, color: str) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """

    game = MinMaxPodaAlphaBeta(the_board, color)

    _, action = game.minmax()

    return action


class MinMaxPodaAlphaBeta:
    def __init__(self, the_board: Board, color: str) -> None:
        self.board: Board = the_board
        self.color: str = color
        self.depth: int = 4
        self.opponent_color: str = self._opponent_color(color)

    def _opponent_color(self, color: str) -> str:
        """
        Return the color of the opponent
        :param color: the player color
        :return: the opponent color
        """
        return "B" if color == "W" else "W"

    def minmax(self) -> Tuple[int, Tuple[int, int]]:
        """
        Returns a move on the board using the MinMax with Alpha-Beta pruning
        :return: the score and the move on the board
        """
        value, action = self._max(self.board, -np.inf, np.inf, self.depth, self.color)
        return value, action

    def _max(self, board: Board, alpha: int, beta: int, depth: int, color: str) -> Tuple[int, Tuple[int, int]]:
        """
        Returns a move that maximize the score
        :param board: the game board
        :param alpha: the alpha used for the pruning
        :param beta: the beta used for the pruning
        :param depth: the depth in the search graph
        :param color: the color of the player
        :return: the value of the alpha and the move on the board
        """
        if depth == 0:
            return self.calculate_points(board, color), None

        best_value = -np.inf
        legal_moves = board.legal_moves(color)

        if len(legal_moves) == 0:
            return 0, (-1, -1)

        action = legal_moves[-1]

        for s in legal_moves:
            board_copy = deepcopy(board)
            board_copy.process_move(s, color)
            value = max(best_value, self._min(board_copy, alpha, beta, depth-1, self._opponent_color(color))[0])

            if value != best_value:
                best_value = value
                action = s

            alpha = max(alpha, best_value)

            if alpha > beta:
                break

        return alpha, action

    def _min(self, board: Board, alpha: int, beta: int, depth: int, color: str) -> Tuple[int, Tuple[int, int]]:
        """
        Returns a move that minimiza the score
        :param board: the game board
        :param alpha: the alpha used for the pruning
        :param beta: the beta used for the pruning
        :param depth: the depth in the search graph
        :param color: the color of the player
        :return: the value of the beta and the move on the board
        """
        if depth == 0:
            return self.calculate_points(board, color), None

        best_value = np.inf
        legal_moves = board.legal_moves(color)

        if len(legal_moves) == 0:
            return 0, (-1, -1)

        action = legal_moves[-1]

        for s in legal_moves:
            board_copy = deepcopy(board)
            board_copy.process_move(s, color)
            value = min(best_value, self._max(board_copy, alpha, beta, depth-1, self._opponent_color(color))[0])

            if value != best_value:
                best_value = value
                action = s

            beta = min(beta, value)

            if beta < alpha:
                break

        return beta, action

    def calculate_points(self, board: Board, color: str) -> int:
        """
        Calculates the score for a color giving the state of the board
        :param board: the game board
        :param color: the color of the player
        :return: the score of the player giving their color
        """
        points = 0

        for i in range(8):
            for j in range(8):
                if board.tiles[i][j] == color:
                    points += 1
        
        return points
