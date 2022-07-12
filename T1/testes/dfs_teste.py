import unittest
from T1.dfs import dfs


class DFSTeste(unittest.TestCase):
    def test_dfs(self):
        self.assertEqual(None, dfs("185423_67"))


if __name__ == '__main__':
    unittest.main()
