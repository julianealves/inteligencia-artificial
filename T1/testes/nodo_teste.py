import unittest
from T1.nodo import Nodo


class NodoTeste(unittest.TestCase):
    def test_calculo_custo(self):
        nodo_pai = Nodo(estado="2_3541687", custo=0, pai=None, acao=None)
        self.assertEqual(nodo_pai.get_custo(), 0)

        nodo_filho1 = Nodo(estado="_23541687", pai=nodo_pai, acao="esquerda", custo=1)
        self.assertEqual(nodo_filho1.get_custo(), 1)

        nodo_filho2 = Nodo(estado="2435_1687", pai=nodo_pai, acao="abaixo", custo=1)
        self.assertEqual(nodo_filho2.get_custo(), 1)

        nodo_filho3 = Nodo(estado="23_541687", pai=nodo_pai, acao="direita", custo=1)
        self.assertEqual(nodo_filho3.get_custo(), 1)

        nodo_filho1_do_filho1 = Nodo(estado="523_41867", pai=nodo_filho1, acao="baixo", custo=2)
        self.assertEqual(nodo_filho1_do_filho1.get_custo(), 2)

        nodo_filho1_do_filho1_do_filho1 = Nodo(estado="5234_1867", pai=nodo_filho1_do_filho1, acao="direita", custo=3)
        self.assertEqual(nodo_filho1_do_filho1_do_filho1.get_custo(), 3)

        nodo_filho1_do_filho3 = Nodo(estado="523_41867", pai=nodo_filho3, acao="baixo", custo=2)
        self.assertEqual(nodo_filho1_do_filho3.get_custo(), 2)

        nodo_nivel4 = Nodo(estado="52341_867", pai=nodo_filho1_do_filho1_do_filho1, acao="direita", custo=4)
        self.assertEqual(nodo_nivel4.get_custo(), 4)


if __name__ == '__main__':
    unittest.main()
