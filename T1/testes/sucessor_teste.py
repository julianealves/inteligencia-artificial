import unittest
from T1.sucessor import sucessor


class SucessorTeste(unittest.TestCase):
    def test_something(self):
        resp = sucessor("2435_1687")
        self.assertEqual(resp[0][0], "direita")
        self.assertEqual(resp[0][1], "24351_687")
        self.assertEqual(resp[1][0], "esquerda")
        self.assertEqual(resp[1][1], "243_51687")
        self.assertEqual(resp[2][0], "acima")
        self.assertEqual(resp[2][1], "2_3541687")
        self.assertEqual(resp[3][0], "abaixo")
        self.assertEqual(resp[3][1], "2435816_7")

        resp = sucessor("_23456781")
        self.assertEqual(resp[0][0], "direita")
        self.assertEqual(resp[0][1], "2_3456781")
        self.assertEqual(resp[1][0], "abaixo")
        self.assertEqual(resp[1][1], "423_56781")

        resp = sucessor("1234567_8")
        self.assertEqual(resp[0][0], "direita")
        self.assertEqual(resp[0][1], "12345678_")
        self.assertEqual(resp[1][0], "esquerda")
        self.assertEqual(resp[1][1], "123456_78")
        self.assertEqual(resp[2][0], "acima")
        self.assertEqual(resp[2][1], "1234_6758")


if __name__ == '__main__':
    unittest.main()
