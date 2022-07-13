import unittest
from T1.solucao import bfs


class BFSTeste(unittest.TestCase):
    def test_bfs(self):
        solucao_otima = ["direita", "direita"]
        self.assertEqual(solucao_otima, bfs("123456_78"))

        self.assertEqual(23, len(bfs("2_3541687")))
        self.assertIsNone(bfs("185423_67"))

        estado = "1235_6478"
        solucao_otima = ["esquerda", "abaixo", "direita", "direita"]
        self.assertEqual(solucao_otima, bfs(estado))


if __name__ == "__main__":
    unittest.main()
