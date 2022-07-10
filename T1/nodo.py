from __future__ import annotations


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