from __future__ import annotations


class Nodo:
    def __init__(self, estado: str, pai: Nodo = None, acao: str = None) -> None:
        """
        Classe Nodo representa um nodo do grafo de busca para a solucao do problem 8-puzzle

        :param estado: representacao do estado ao qual ese no se refere (e.g.: '_23541687')
        :param pai: referencia ao no que precede este
        :param acao: acao que foi aplicada ao no pai para gerar este
        """
        self.estado: str = estado
        self.pai: Nodo = pai
        self.acao: str = acao
        self.custo: int = self._calcula_custo(self.pai)

    def _calcula_custo(self, nodo: Nodo) -> int:
        """
        Calcula o custo do caminho a partir do estado inicial ate este nodo

        :param nodo: referencia ao nodo pai para a recursao
        :return: custo do nodo ate o estado inicial do grafo
        """
        if nodo is None:
            return 0
        else:
            return 1 + self._calcula_custo(nodo.pai)

    def get_custo(self) -> int:
        """
        :return: custo do nodo ate o estado inicial do grafo
        """
        return self.custo
