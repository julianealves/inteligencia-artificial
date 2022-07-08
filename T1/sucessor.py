from typing import List


def sucessor(estado: str) -> List:
    """
    O metodo retorna uma lista de tuplas onde cada tupla contem cada ação que pode
    ser realizada no estado recebido como parametro
    :param estado: Recebe o e estado atual do 8-puzzle (e.g.: '_23541687')
    :return: Lista de tuplas com as informacoes (ação, estado atingido)
    """

    listSucessores = []

    posicao = estado.find('_')

    if posicao != 2 and posicao != 5 and posicao != 8:
        caracter = estado[posicao + 1]
        posicaoSucessor = estado[:posicao] + caracter + '_' + estado[posicao + 2:]
        strSucessor = ("direita", posicaoSucessor)
        listSucessores.append(strSucessor)

    if posicao != 0 and posicao != 3 and posicao != 6:
        caracter = estado[posicao - 1]
        posicaoSucessor = estado[:posicao - 1] + '_' + caracter + estado[posicao + 1:]
        strSucessor = ("esquerda", posicaoSucessor)
        listSucessores.append(strSucessor)

    if posicao != 0 and posicao != 1 and posicao != 2:
        caracter = estado[posicao - 3]
        posicaoSucessor = estado[:posicao - 3] + '_' + estado[posicao - 2:posicao] + caracter + estado[posicao + 1:]
        strSucessor = ("acima", posicaoSucessor)
        listSucessores.append(strSucessor)

    if posicao != 6 and posicao != 7 and posicao != 8:
        caracter = estado[posicao + 3]
        posicaoSucessor = estado[:posicao] + caracter + estado[posicao + 1:posicao + 3] + '_' + estado[posicao + 4:]
        strSucessor = ("abaixo", posicaoSucessor)
        listSucessores.append(strSucessor)

    return listSucessores
