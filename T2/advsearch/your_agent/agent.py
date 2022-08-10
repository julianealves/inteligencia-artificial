import random
import sys
from advsearch.othello.board import Board
import numpy as np
from copy import deepcopy

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta

    game = MinMaxPodaAlphaBeta(the_board, color)

    _, action = game.minmax()

    return action


class MinMaxPodaAlphaBeta:
    def __init__(self, the_board, color):
        self.board = the_board
        self.color = color
        self.depth = 4

    def minmax(self):
        value, action = self._max(self.board, -np.inf, np.inf, self.depth)
        return value, action

    def _max(self, board, alpha, beta, depth):
        if depth == 0:
            return self.calculate_points(board), None

        value = -np.inf
        action = None

        legal_moves = board.legal_moves(self.color)

        if len(legal_moves) == 0:
            return 0, (-1, -1)

        for s in legal_moves:
            board_copy = deepcopy(board)
            board_copy.process_move(s, self.color)
            value = max(value, self._min(board_copy, alpha, beta, depth-1)[0])
            action = s
            alpha = max(alpha, value)

            if alpha > beta:
                break

        return alpha, action

    def _min(self, board, alpha, beta, depth):
        if depth == 0:
            return self.calculate_points(board), None

        value = np.inf
        action = None

        legal_moves = board.legal_moves(self.color)

        if len(legal_moves) == 0:
            return 0, (-1, -1)

        for s in legal_moves:
            board_copy = deepcopy(board)
            board_copy.process_move(s, self.color)
            value = min(value, self._max(board_copy, alpha, beta, depth-1)[0])
            action = s
            alpha = min(beta, value)

            if beta < alpha:
                break

        return beta, action

    def calculate_points(self, board):
        """
        Metodo que calcula os pontos dado o estado atual do board
        """
        return random.randint(0, 9)
