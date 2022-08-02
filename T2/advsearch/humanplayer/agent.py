from advsearch.othello import board


def make_move(the_board, color):
    move = input("Você é o jogador {}. Escreva sua jogada (<coluna> <linha>): ".format("W" if color == "W" else "B"))
    x = -1
    y = -1

    try:
        x, y = move.split()
        ok = True
    except ValueError:
        ok = False

    while not ok or not the_board.is_legal((int(y), int(x)), color):
        move = input("Sua jogada foi ilegal, tente outra vez: ")

        try:
            x, y = move.split()
            ok = True
        except ValueError:
            ok = False

    return int(x), int(y)
