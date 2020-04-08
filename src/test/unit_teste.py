import unittest
from softdes import lambda_handler

class Test(unittest.TestCase):
    def test_answer(self):
        res = lambda_handler("errado", '')
        self.assertEqual(res, "Função inválida.")

        args = {'ndes': '1', 'code': 'def desafio1(n):\n    return 0\n    # return n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        self.assertEqual(res, "")