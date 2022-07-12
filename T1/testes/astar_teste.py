import unittest
from T1.astar import astar_hamming, astar_manhattan


class AstarTeste(unittest.TestCase):
    def test_astar(self):
        self.assertEqual(23, len(astar_hamming("2_3541687")))
        self.assertEqual(23, len(astar_manhattan("2_3541687")))

        estado = "1235_6478"
        solucao_otima = ["esquerda", "abaixo", "direita", "direita"]
        self.assertEqual(solucao_otima, astar_hamming(estado))
        self.assertEqual(solucao_otima, astar_manhattan(estado))

        estado = "123456_78"
        solucao_otima = ["direita", "direita"]
        self.assertEqual(solucao_otima, astar_hamming(estado))
        self.assertEqual(solucao_otima, astar_manhattan(estado))

        self.assertEqual(14, len(astar_hamming("8134_2765")))
        self.assertEqual(14, len(astar_manhattan("8134_2765")))

        self.assertIsNone(astar_manhattan("185423_67"))
        self.assertIsNone(astar_hamming("185423_67"))
        self.assertIsNone(astar_manhattan("12345687_"))
        self.assertIsNone(astar_hamming("12345687_"))


if __name__ == "__main__":
    unittest.main()
