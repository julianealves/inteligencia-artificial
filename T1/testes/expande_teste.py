import unittest
from T1.expande import expande
from T1.nodo import Nodo


class ExpandeTeste(unittest.TestCase):
    def test_expande(self):
        nodo_pai = Nodo(estado="2_3541687", custo=0, pai=None, acao=None)
        nodo_filho1 = Nodo(estado="_23541687", pai=nodo_pai, acao="esquerda", custo=1)
        nodo_filho2 = Nodo(estado="2435_1687", pai=nodo_pai, acao="abaixo", custo=1)
        nodo_filho3 = Nodo(estado="23_541687", pai=nodo_pai, acao="direita", custo=1)
        nodo_filho4 = Nodo(estado="24351_687", pai=nodo_filho2, acao="direita", custo=2)

        sucessores = expande(nodo_pai)

        self.assertEqual(sucessores[0].estado, "23_541687")
        self.assertEqual(sucessores[0].acao, "direita")
        self.assertEqual(sucessores[0].custo, 1)

        self.assertEqual(sucessores[1].estado, "_23541687")
        self.assertEqual(sucessores[1].acao, "esquerda")
        self.assertEqual(sucessores[1].custo, 1)

        self.assertEqual(sucessores[2].estado, "2435_1687")
        self.assertEqual(sucessores[2].acao, "abaixo")
        self.assertEqual(sucessores[2].custo, 1)

        sucessores = expande(nodo_filho1)

        self.assertEqual(sucessores[0].estado, "2_3541687")
        self.assertEqual(sucessores[0].acao, "direita")
        self.assertEqual(sucessores[0].custo, 2)

        self.assertEqual(sucessores[1].estado, "523_41687")
        self.assertEqual(sucessores[1].acao, "abaixo")
        self.assertEqual(sucessores[1].custo, 2)

        sucessores = expande(nodo_filho3)

        self.assertEqual(sucessores[0].estado, "2_3541687")
        self.assertEqual(sucessores[0].acao, "esquerda")
        self.assertEqual(sucessores[0].custo, 2)

        self.assertEqual(sucessores[1].estado, "23154_687")
        self.assertEqual(sucessores[1].acao, "abaixo")
        self.assertEqual(sucessores[1].custo, 2)

        sucessores = expande(nodo_filho4)

        self.assertEqual(sucessores[0].estado, "2435_1687")
        self.assertEqual(sucessores[0].acao, "esquerda")
        self.assertEqual(sucessores[0].custo, 3)

        self.assertEqual(sucessores[1].estado, "24_513687")
        self.assertEqual(sucessores[1].acao, "acima")
        self.assertEqual(sucessores[1].custo, 3)

        self.assertEqual(sucessores[2].estado, "24351768_")
        self.assertEqual(sucessores[2].acao, "abaixo")
        self.assertEqual(sucessores[2].custo, 3)

        pai = Nodo("185432_67", None, "abaixo", 2)  # o pai do pai esta incorreto, mas nao interfere no teste
        # a resposta esperada deve conter nodos com os seguintes atributos (ordem dos nodos nao importa)
        resposta_esperada = {
            ("185_32467", pai, "acima", 3),
            ("1854326_7", pai, "direita", 3),
        }

        resposta = expande(pai)  # obtem a resposta chamando a funcao implementada
        self.assertEqual(2, len(resposta))  # verifica se foram retornados 2 nodos
        for nodo in resposta:
            # verifica se a tupla com os atributos do nodo esta' presente no conjunto com os nodos esperados
            self.assertIn((nodo.estado, nodo.pai, nodo.acao, nodo.custo), resposta_esperada)


if __name__ == '__main__':
    unittest.main()
