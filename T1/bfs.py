from typing import List
from nodo import Nodo
from expande import expande
import time

def caminho_s_v_bfs(nodo: Nodo, caminho: List) -> List:
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

def ja_explorado(explorados: dict, v: Nodo) -> bool:
    try:
        nodo = explorados[v]
    except KeyError:
        nodo = None
    return nodo is not None

def bfs (estado: str) -> List:
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
            return caminho_s_v_bfs(v, [])

        if not ja_explorado(explorados, v):
            explorados[v] = 0
            visitados[v.estado] = v.get_custo()
            vizinhos = expande(v)
            for s in vizinhos:
                if estado_nao_visitado(visitados, s) and estado_nao_fronteira(estados_fronteira, s):
                    fronteira.append(s)
                    estados_fronteira[s.estado] = s.get_custo()

    return None

def estado_nao_fronteira(estados_fronteira: dict, s: Nodo) -> bool:
    try:
        custo = estados_fronteira[s.estado]
    except KeyError:
        custo = None
    return custo is None


def ja_explorado(explorados: dict, v: Nodo) -> bool:
    try:
        nodo = explorados[v]
    except KeyError:
        nodo = None
    return nodo is not None


def estado_nao_visitado(estados_explorados: dict, s: Nodo) -> bool:
    try:
        custo = estados_explorados[s.estado]
    except KeyError:
        custo = None

    return custo is None

def main():
    inicio = time.time()
    n = bfs("2_3541687")
    fim = time.time()
    print(f"Tempo execução: {fim - inicio}")
    print(n)

    return 0

if __name__ == "__main__":
    main()