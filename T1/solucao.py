from __future__ import annotations
import heapq
from typing import List, Optional
import time
import utils as utils


class Nodo(object):
    def __init__(self, estado: str, pai: Nodo, acao: str, custo: int) -> None:
        """
        Classe Nodo representa um nodo do grafo de busca para a solucao do problem 8-puzzle

        :param estado: representacao do estado ao qual ese no se refere (e.g.: '_23541687')
        :param pai: referencia ao no que precede este
        :param acao: acao que foi aplicada ao no pai para gerar este
        """
        self.estado: str = estado
        self.pai: Nodo = pai
        self.acao: str = acao
        self.custo: int = custo
        self.funcao = 0

    def calcula_custo(self) -> int:
        """
        Calcula o custo do caminho a partir do estado inicial ate este nodo

        :return: custo do nodo ate o estado inicial do grafo
        """

        return 1 + self.pai.get_custo()

    def get_custo(self) -> int:
        """
        :return: custo do nodo ate o estado inicial do grafo
        """
        return self.custo

    def set_custo(self, custo: int) -> None:
        """
        :param custo: custo do nodo ate o estado inicial do grafo
        :return: None
        """
        self.custo = custo

    def set_funcao(self, funcao: int) -> None:
        self.funcao = funcao

    def __lt__(self, other):
        return self.lt(self.funcao, other.funcao)

    def lt(self, funcao1, funcao2):
        return funcao1 < funcao2


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


def expande(nodo: Nodo) -> List:
    """
    Metodo recebe um nodo e retorna uma lista com todos os nodos sucessores a este

    :param nodo: Recebe o nodo a ser expandido
    :return: Lista com os nodos sucessores
    """

    listOfNodes = []
    listOfSucc = sucessor(nodo.estado)

    for acao, estado in listOfSucc:
        nodoSucc = Nodo(estado=estado, pai=nodo, acao=acao, custo=0)
        # atualiza custo
        nodoSucc.set_custo(nodoSucc.calcula_custo())
        listOfNodes.append(nodoSucc)

    return listOfNodes


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
    f = nodo_raiz.get_custo() + utils.hamming(estado)
    nodo_raiz.set_funcao(f)
    heapq.heappush(fronteira, nodo_raiz)

    while len(fronteira) != 0:
        v = heapq.heappop(fronteira)
        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return utils.caminho_s_v_recursao(v, [])
        if not utils.ja_explorado_astar(explorados, v):
            explorados[v] = 0
            estados_explorados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                # verifica se estado ja foi visitado
                if utils.estado_nao_visitado_astar(estados_explorados, s):
                    f = s.get_custo() + utils.hamming(s.estado)
                    s.set_funcao(f)
                    heapq.heappush(fronteira, s)
                    estados_fronteira[s.estado] = s.get_custo()
                if utils.estado_com_menor_custo_astar(estados_fronteira, s):
                    continue
    return None


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
    f = nodo_raiz.get_custo() + utils.manhattan(estado)
    nodo_raiz.set_funcao(f)
    heapq.heappush(fronteira, nodo_raiz)

    while len(fronteira) != 0:
        v = heapq.heappop(fronteira)
        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return utils.caminho_s_v_recursao(v, [])
        if not utils.ja_explorado_astar(explorados, v):
            explorados[v] = 0
            estados_explorados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                # verifica se estado ja foi visitado
                if utils.estado_nao_visitado_astar(estados_explorados, s):
                    f = s.get_custo() + utils.manhattan(s.estado)
                    s.set_funcao(f)
                    heapq.heappush(fronteira, s)
                    estados_fronteira[s.estado] = s.get_custo()
                if utils.estado_com_menor_custo_astar(estados_fronteira, s):
                    continue
    return None


def bfs(estado: str) -> Optional[List]:
    """
    Metodo executa o algoritmo BFS para achar os movimentos que solucionam o 8-puzzle dado o estado inicial.
    Caso nao exista solucao, retorna None.

    :param estado: estado inicial
    :return: lista de movimentos para solucionar o 8-puzzle
    """
    nodo_raiz = Nodo(estado=estado, pai=None, acao=None, custo=0)
    solucao = "12345678_"
    explorados = {}
    fronteira = [nodo_raiz]
    estados_fronteira = {}
    visitados = {}

    while len(fronteira) != 0:

        v = fronteira[0]
        del fronteira[0]

        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return utils.caminho_s_v(v, [])

        if not utils.ja_explorado_astar(explorados, v):
            explorados[v] = 0
            visitados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                if utils.estado_nao_visitado_astar(visitados, s) and utils.estado_nao_fronteira(estados_fronteira, s):
                    fronteira.append(s)
                    estados_fronteira[s.estado] = s.get_custo()

    return None


def dfs(estado: str) -> Optional[List]:
    """
    Metodo executa o algoritmo DFS para achar os movimentos que solucionam o 8-puzzle dado o estado inicial.
    Caso nao exista solucao, retorna None.

    :param estado: estado inicial
    :return: lista de movimentos para solucionar o 8-puzzle
    """

    nodo_raiz = Nodo(estado=estado, pai=None, acao=None, custo=0)
    solucao = "12345678_"
    explorados = {}
    visitados = {}
    fronteira : List[Nodo] = [nodo_raiz]
    estados_fronteira = {}

    while len(fronteira) != 0:

        v = fronteira.pop()

        if v.estado == solucao:
            print(f"Nós expandidos: {len(explorados)}")
            print(f"Custo: {v.get_custo()}")
            return utils.caminho_s_v(v, [])

        if not utils.ja_explorado_astar(explorados, v):
            explorados[v] = 0
            visitados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                if utils.estado_nao_visitado_astar(visitados, s) and utils.estado_nao_fronteira(estados_fronteira, s):
                    fronteira.append(s)
                    estados_fronteira[s.estado] = s.get_custo()

    return None


if __name__ == "__main__":
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

    print("*** DFS ***")
    inicio = time.time()
    caminho = dfs("2_3541687")
    fim = time.time()
    print(f"Tempo execução: {fim - inicio}")
    # print(caminho)

    print("*** BFS ***")
    inicio = time.time()
    caminho = bfs("2_3541687")
    fim = time.time()
    print(f"Tempo execução: {fim - inicio}")
    print(caminho)
