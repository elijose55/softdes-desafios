import unittest
import os.path as path
import sys

absolute_path = path.abspath(path.join(__file__ ,"../.."))
sys.path.insert(0, absolute_path + '/src')


from softdes import lambda_handler

class Test(unittest.TestCase):
    def test_resposta_formato_errado(self):
        args = {'ndes': '1', 'code': 'def desafio1(n):\n    return 0\n    # return n\n'}
        res = lambda_handler(args, '')
        self.assertEqual(res, "Função inválida.")

    def test_resposta_correta(self):
        args = {'ndes': '1', 'code': 'def desafio1(n):\n    return 0\n    # return n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        self.assertEqual(res, "")

    def test_resposta_funcao_incorreta(self):
        args = {'ndes': '1', 'code': 'def desafio1(n):\n    return n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        self.assertEqual(res, "a b c")

    def test_resposta_nome_funcao_invalido(self):
        args = {'ndes': '1', 'code': 'def desafio2(n):\n    return 0\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        self.assertEqual(res, "Nome da função inválido. Usar 'def desafio1(...)'")

    def test_primeira_resposta_incorreta(self):
        args = {'ndes': '1', 'code': 'def desafio1(n):\n    return 0\n', 'args': [[1], [2], [3]], 'resp': [1, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        print("H", res)
        self.assertEqual(res, "a")

    def test_resposta_numero_desafio(self):
        args = {'ndes': '2', 'code': 'def desafio2(n):\n    return 0\n    # return n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
        res = lambda_handler(args, '')
        self.assertEqual(res, "")