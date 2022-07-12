from typing import List
import heapq
from typing import Optional
from nodo import Nodo
from expande import expande


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


def caminho_s_v(nodo: Nodo, caminho: List) -> List:
    """
    Retorna o caminho para a solucao otima
    :param nodo: Nodo com a solucao
    :param caminho: Lista vazia para retornar o caminho S-V
    :return: Lista contendo o caminho da raiz ate o nodo
    """
    if nodo.acao is None:
        return []
    caminho_s_v(nodo.pai, caminho)
    caminho.append(nodo.acao)
    return caminho


def astar_hamming(estado: str) -> Optional[List]:
    """
    Metodo executa o algoritmo A* para achar os movimentos que solucionam o 8-puzzle dado o estado inicial.
    Caso nao exista solucao, retorna None.
    A heuristica utilizada e a Hamming.
    :param estado: estado inicial
    :return: lista de movimentos para solucionar o 8-puzzle
    """
    solucao = "12345678_"
    explorados = {}
    fronteira = []
    estados_explorados = {}
    estados_fronteira = {}
    nodo_raiz = Nodo(estado=estado, pai=None, acao=None, custo=0)
    # f(v) = g(v) + h(v), onde g(v) eh o custo do caminho do estado inicial ate v e h(v) eh a distancia heuristica
    f = nodo_raiz.get_custo() + hamming(estado)
    nodo_raiz.set_funcao(f)
    heapq.heappush(fronteira, nodo_raiz)

    while len(fronteira) != 0:
        v = heapq.heappop(fronteira)
        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return caminho_s_v(v, [])
        if not ja_explorado(explorados, v):
            explorados[v] = 0
            estados_explorados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                # verifica se estado ja foi visitado
                if estado_ja_visitado(estados_explorados, s):
                    f = s.get_custo() + hamming(s.estado)
                    s.set_funcao(f)
                    heapq.heappush(fronteira, s)
                    estados_fronteira[s.estado] = s.get_custo()
                if estado_com_menor_custo(estados_fronteira, s):
                    continue
    return None


def ja_explorado(explorados: dict, v: Nodo) -> bool:
    try:
        nodo = explorados[v]
    except KeyError:
        nodo = None
    return nodo is not None


def astar_manhattan(estado: str) -> Optional[List]:
    """
    Metodo executa o algoritmo A* para achar os movimentos que solucionam o 8-puzzle dado o estado inicial.
    Caso nao exista solucao, retorna None.
    A heuristica utilizada e a Manhattan.
    :param estado: estado inicial
    :return: lista de movimentos para solucionar o 8-puzzle
    """
    solucao = "12345678_"
    explorados = {}
    fronteira = []
    estados_explorados = {}
    estados_fronteira = {}
    nodo_raiz = Nodo(estado=estado, pai=None, acao=None, custo=0)
    # f(v) = g(v) + h(v), onde g(v) eh o custo do caminho do estado inicial ate v e h(v) eh a distancia heuristica
    f = nodo_raiz.get_custo() + manhattan(estado)
    nodo_raiz.set_funcao(f)
    heapq.heappush(fronteira, nodo_raiz)

    while len(fronteira) != 0:
        v = heapq.heappop(fronteira)
        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return caminho_s_v(v, [])
        if not ja_explorado(explorados, v):
            explorados[v] = 0
            estados_explorados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                # verifica se estado ja foi visitado
                if estado_ja_visitado(estados_explorados, s):
                    f = s.get_custo() + manhattan(s.estado)
                    s.set_funcao(f)
                    heapq.heappush(fronteira, s)
                    estados_fronteira[s.estado] = s.get_custo()
                if estado_com_menor_custo(estados_fronteira, s):
                    continue
    return None


def estado_com_menor_custo(estados_fronteira: dict, s: Nodo) -> bool:
    try:
        custo = estados_fronteira[s.estado]
    except KeyError:
        custo = None

    return custo is not None and estados_fronteira[s.estado] < s.get_custo()


def estado_ja_visitado(estados_explorados: dict, s: Nodo) -> bool:
    try:
        custo = estados_explorados[s.estado]
    except KeyError:
        custo = None

    return (custo is None) or (custo is not None and s.get_custo() < estados_explorados[s.estado])


if __name__ == "__main__":
    import time

    print("*** A* - Hamming ***")
    inicio = time.time()
    estado = "2_3541687"
    caminho = astar_hamming(estado)
    fim = time.time()
    print(f"Tempo execução Hamming: {fim - inicio}")
    print(f"Caminho: {caminho}")

    print("*** A* - Manhattan ***")
    inicio = time.time()
    estado = "2_3541687"
    caminho = astar_manhattan(estado)
    fim = time.time()
    print(f"Tempo execução Manhattan: {fim - inicio}")
    print(f"Caminho: {caminho}")
