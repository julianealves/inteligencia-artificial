import unittest
from T1.expande import expande
from T1.nodo import Nodo


class ExpandeTeste(unittest.TestCase):
    def test_something(self):
        nodo_pai = Nodo(estado="2_3541687")
        nodo_filho1 = Nodo(estado="_23541687", pai=nodo_pai, acao="esquerda")
        nodo_filho2 = Nodo(estado="2435_1687", pai=nodo_pai, acao="abaixo")
        nodo_filho3 = Nodo(estado="23_541687", pai=nodo_pai, acao="direita")
        nodo_filho4 = Nodo(estado="24351_687", pai=nodo_filho2, acao="direita")

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


if __name__ == '__main__':
    unittest.main()
