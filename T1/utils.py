from __future__ import annotations
from typing import List
import solucao as solucao


def hamming(estado: str) -> int:
    """
    Calcula o numero de pecas fora do lugar para o 8-puzzle
    :param estado: Estado atual do 8-puzzle
    :return: Numero de pecas fora do lugar
    """
    h = 0
    solucao = "12345678_"
    for i in range(9):
        if estado[i] != solucao[i]:
            h = h + 1
    # Retorna -1 para ignorar o espaco
    return h - 1


def manhattan(estado: str) -> int:
    """
    Calcula a soma da distancia Manhattan de cada a peca para seus respectivos lugares correto
    :param estado: Estado atual do 8-puzzle
    :return: Soma da distancia manhattan
    """
    h = 0
    solucao = "12345678_"
    # estado = estado.replace("_", "")
    coordenadas_pecas = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                         "4": (1, 0), "5": (1, 1), "6": (1, 2),
                         "7": (2, 0), "8": (2, 1), "9": (2, 2)}
    for s in solucao:
        if s == "_":
            continue
        coordenadas_atual = coordenadas_pecas[str(estado.find(s) + 1)]
        coordenadas_esperada = coordenadas_pecas[s]

        h = h + (abs(coordenadas_atual[0] - coordenadas_esperada[0]) + abs(
            coordenadas_atual[1] - coordenadas_esperada[1]))

    return h


def caminho_s_v_recursao(nodo: solucao.Nodo, caminho: List) -> List:
    """
    Retorna o caminho para a solucao otima
    :param nodo: Nodo com a solucao
    :param caminho: Lista vazia para retornar o caminho S-V
    :return: Lista contendo o caminho da raiz ate o nodo
    """
    if nodo.acao is None:
        return []
    caminho_s_v_recursao(nodo.pai, caminho)
    caminho.append(nodo.acao)
    return caminho


def ja_explorado_astar(explorados: dict, v: solucao.Nodo) -> bool:
    try:
        nodo = explorados[v]
    except KeyError:
        nodo = None
    return nodo is not None


def estado_com_menor_custo_astar(estados_fronteira: dict, s: solucao.Nodo) -> bool:
    try:
        custo = estados_fronteira[s.estado]
    except KeyError:
        custo = None

    return custo is not None and estados_fronteira[s.estado] < s.get_custo()


def estado_nao_visitado_astar(estados_explorados: dict, s: solucao.Nodo) -> bool:
    try:
        custo = estados_explorados[s.estado]
    except KeyError:
        custo = None

    return (custo is None) or (custo is not None and s.get_custo() < estados_explorados[s.estado])


def caminho_s_v(nodo: solucao.Nodo, caminho: List) -> List:
    """
    Retorna o caminho para a solucao otima
    :param nodo: Nodo com a solucao
    :param caminho: Lista vazia para retornar o caminho S-V
    :return: Lista contendo o caminho da raiz ate o nodo
    """
    while nodo.acao is not None:
        caminho.append(nodo.acao)
        nodo = nodo.pai
    caminho.reverse()
    return caminho


def estado_nao_fronteira(estados_fronteira: dict, s: solucao.Nodo) -> bool:
    try:
        custo = estados_fronteira[s.estado]
    except KeyError:
        custo = None
    return custo is None


def ja_explorado(explorados: dict, v: solucao.Nodo) -> bool:
    try:
        nodo = explorados[v]
    except KeyError:
        nodo = None
    return nodo is not None


def estado_nao_visitado(estados_explorados: dict, s: solucao.Nodo) -> bool:
    try:
        custo = estados_explorados[s.estado]
    except KeyError:
        custo = None

    return custo is None