import os
import sys
import time
import importlib
import argparse
import xml.etree.ElementTree as ET
import xml.dom.minidom
from pytermgui import tim, ansi_interface  # for TUI (text user interface)

import advsearch.othello.board as board
import advsearch.timer as timer


def player_name(player_dir:str) -> str:
    """
    Removes leading 'advsearch.' or 'advsearch/' from the player directory
    :param player_dir:
    :return:
    """
    if player_dir.startswith('advsearch'):
        return player_dir[len('advsearch')+1:]  # +1 to account for the / or .


class Server(object):
    """
    Othello server, implements a simple file-based playing protocol

    """

    SCREEN_BOARD_POSITION = (0, 2)  # col, row of board position on screen

    def __init__(self, p1_dir, p2_dir, delay, history, output, pace=0):
        """
        Initializes the Othello game server
        :param p1_dir: directory where the 'agent.py' of the 1st player is located
        :param p2_dir: directory where the 'agent.py' of the 2nd player is located
        :param delay: time limit to make a move
        :param history: file that will contain the match history (plain text)
        :param output: file to save game details (includes history)
        :param pace: time to wait to display a move, if a player returns before timeout
        """
        # normalizes paths to avoid errors with trailing slashes
        p1_dir = os.path.normpath(p1_dir)
        p2_dir = os.path.normpath(p2_dir)

        self.basedir = os.path.abspath('.')

        self.player_dirs = [p1_dir, p2_dir]

        self.player_colors = [board.Board.BLACK, board.Board.WHITE]
        self.color_names = ['black', 'white']
        self.board = board.Board()

        self.history = []  # a list of performed moves (tuple: ((x,y), color)
        self.history_file = open(history, 'w')
        self.output_file = output

        self.delay = delay
        self.pace = pace

        self.result = None

        # start and finish times of match
        self.start = None
        self.finish = None

        # imports 'agent.py' from both players
        p1_module = p1_dir.replace(os.sep, '.')
        p2_module = p2_dir.replace(os.sep, '.')
        self.player_modules = [
            importlib.import_module(f"{p1_module}.agent"),
            importlib.import_module(f"{p2_module}.agent"),
        ]

    def __del__(self):
        self.history_file.close()

    def print_header(self):
        tim.print(
            f'[@green]{player_name(self.player_dirs[0])} ({self.board.num_pieces(board.Board.BLACK):02d} [black]⬤[/fg]) '
            f'x ([ffffff]⬤[/fg] {self.board.num_pieces(board.Board.WHITE):02d}) [@green]{player_name(self.player_dirs[1])} [/bg]'
        )

    def display_board(self, move=None, flipped=False) -> None:
        """
        Displays the board on screen
        :param move: move position to highlight or None
        :param flipped: whether to highlight latest flipped pieces
        :return:
        """
        ansi_interface.move_cursor(self.SCREEN_BOARD_POSITION)
        tim.print(self.board.decorated_str(move=move, highlight_flipped=flipped))
        sys.stdout.flush()
        time.sleep(1)  # waits 1s for board visualization

    def run(self):
        self.start = time.localtime()
        player = 0
        latest_move = None
        illegal_count = [0, 0]  # counts the number of illegal move attempts

        ansi_interface.clear()
        sys.stdout.flush()

        while True:  # runs until endgame
            start = time.time()
            # checks whether players have available moves
            no_moves_current = len(self.board.legal_moves(self.player_colors[player])) == 0
            no_moves_opponent = len(self.board.legal_moves(self.board.opponent(self.player_colors[player]))) == 0

            # calculates scores
            p1_score = self.board.num_pieces(self.board.BLACK) #sum([1 for char in str(self.board) if char == self.board.BLACK])
            p2_score = self.board.num_pieces(self.board.WHITE) #sum([1 for char in str(self.board) if char == self.board.WHITE])

            ansi_interface.cursor_home()
            self.print_header()
            self.display_board()

            ansi_interface.clear('eos')

            # disqualify player if he attempts illegal moves 5 times in a row
            if illegal_count[player] >= 5:
                print(f'Player {player+1} ({self.player_dirs[player]}) DISQUALIFIED! Too many illegal move attempts or timeouts.')
                print('Game finished!')
                # print('Player 1 (B): %d' % p1_score)
                # print('Player 2 (W): %d' % p2_score)

                self.result = 1 - player
                self.finish = time.localtime()
                self.display_board()
                return self.result

            # checks whether both players don't have available moves (end of game)
            if no_moves_current and no_moves_opponent:

                print('Game finished!')
                #print(f'Player 1 (B - {player_name(self.player_dirs[0])}: {p1_score}')
                #print(f'Player 2 (W - {player_name(self.player_dirs[1])}): {p2_score}')

                if p1_score > p2_score:
                    print(f'Player 1 (B - {self.player_dirs[0]} wins!')
                elif p2_score > p1_score:
                    print(f'Player 2 (W - {self.player_dirs[1]}) wins!')
                else:
                    print('Draw!')

                self.result = 0 if p1_score > p2_score else 1 if p2_score > p1_score else 2
                self.finish = time.localtime()
                return self.result

            # if current player has no moves, toggle player and continue
            if no_moves_current:
                print(f'Player {player+1} ({self.player_dirs[player]}) has no legal moves and will not play this turn.')
                # illegal_count[player] = 0
                player = 1 - player
                time.sleep(self.pace)
                continue

            # creates a copy of the board, so that player changes won't affect mine
            board_copy = self.board.copy()

            # calls current player's make_move function with the specified timeout
            function_call = timer.FunctionTimer(self.player_modules[player].make_move, (board_copy, self.player_colors[player]))
            
            delay = 60 if self.player_dirs[player] == "advsearch.humanplayer" else self.delay
            latest_move = function_call.run(delay)

            # checks for timeout
            if latest_move is None:  # detects timeout
                print('Player %d TIMED OUT and lost its turn. Illegal moves count incremented' % (player + 1))
                illegal_count[player] += 1
                #player = 1 - player
                #continue
                latest_move = -2, -2  # -2 is my code for timeout

            move_x, move_y = latest_move

            # checks for move validity
            if not isinstance(move_x, int) or not isinstance(move_y, int):
                print(f'ILLEGAL MOVE! x, y are {type(move_x)}, {type(move_y)} but should be integer!')
                move_x = move_y = -1  # -1 is my code for type error
                illegal_count[player] += 1

            # prints the board with a highlight on the move before flipping the pieces
            if self.board.is_legal((move_y, move_x), self.player_colors[player]):
                self.display_board(move=(move_y, move_x))

            # saves move in history
            self.history_file.write('%d,%d,%s\n' % (move_x, move_y, self.player_colors[player]))
            self.history.append(((move_x, move_y), self.player_colors[player]))

            if self.board.process_move((move_x, move_y), self.player_colors[player]):
                # illegal_count[player] = 0
                print('Player %d move %d,%d accepted.' % (player + 1, move_x, move_y))
                self.display_board(move=(move_y, move_x), flipped=True)

            else:
                illegal_count[player] += 1
                print('Player %d move %d,%d ILLEGAL!' % (player + 1, move_x, move_y))

            elapsed = time.time() - start  # calculates time spend to process this move
            if self.pace - elapsed > 0:
                time.sleep(self.pace - elapsed)

            ansi_interface.clear("eos")  # clears the remainder of the screen
            #cursor_y, cursor_x, = ansi_interface.report_cursor()
            #if cursor_y == 1:
            #    print('\n' * 3)
            #tim.print(self.board.decorated_str(highlight=(move_y, move_x), colsep=False))

            ansi_interface.cursor_home()  # resets cursor to print all over

            # toggle player for next move
            player = 1 - player

    def write_output(self):
        """
        Writes a xml file with detailed match data
        :return:
        """
        os.chdir(self.basedir)

        root = ET.Element('othello-match')

        colors = [self.board.BLACK, self.board.WHITE, 'None']
        self.player_dirs.append('None')  # trick for writing a draw match

        timing = ET.SubElement(root, 'timing')
        timing.set('start', time.asctime(self.start))
        timing.set('finish', time.asctime(self.finish))

        scores = [self.board.piece_count['B'], self.board.piece_count['W']]

        for idx, p in enumerate(self.player_dirs[:2]):
            elem = ET.SubElement(root, 'player%d' % (idx + 1))
            elem.set('directory', p)
            elem.set('color', colors[idx])

            result = 'win' if scores[idx] > scores[idx - 1] else 'loss' if scores[idx] < scores[idx - 1] else 'draw'
            elem.set('result', result)
            elem.set('score', str(scores[idx]))

        moves = ET.SubElement(root, 'moves')

        for coords, color in self.history:
            move = ET.SubElement(moves, 'move')
            move.set('coord', '%d,%d' % coords)
            move.set('color', color)

        # preety xml thanks to: https://stackoverflow.com/a/1206856/1251716
        ugly_xml = ET.tostring(root).decode('utf-8')
        dom = xml.dom.minidom.parseString(ugly_xml)  # or xml.dom.minidom.parseString(xml_string)
        pretty_xml = dom.toprettyxml()
        f = open(self.output_file, 'w')
        f.write(pretty_xml)
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Othello server.')
    parser.add_argument('players', metavar='player', type=str, nargs=2,
                        help='Path to player directory')
    parser.add_argument('-d', '--delay', type=float, metavar='delay',
                        default=5.0,
                        help='Time allocated for players to make a move.')

    parser.add_argument('-p', '--pace', type=float,
                        default=0,
                        help='Pace of the match: time to wait to display a move '
                             '(if a player returns a move before the delay/timeout).')

    parser.add_argument('-l', '--log-history', type=str, dest='history',
                        default='history.txt', metavar='log-history',
                        help='File to save game log (history).')

    parser.add_argument('-o', '--output-file', type=str, dest='output',
                        default='results.xml', metavar='output-file',
                        help='File to save game details (includes history)')

    args = parser.parse_args()
    p1, p2 = args.players

    s = Server(p1, p2, args.delay, args.history, args.output, args.pace)
    s.run()
    s.write_output()
