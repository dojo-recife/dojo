# Caixa Eletrônico - Resolução
# Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
#
# Entregar o menor número de notas;
# É possível sacar o valor solicitado com as notas disponíveis;
# Saldo do cliente infinito;
# Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
# Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
# Exemplos:
#
# Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
# Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.

from unittest import TestCase
import unittest
from main import *
import random
class Test(TestCase):
    def test_sacar_10_reais(self):
        self.assertEqual(retorna_saque(10), [10])

    def test_sacar_30_reais(self):
        self.assertEqual((retorna_saque(30)), [20, 10])

    def test_sacar_40_reais(self):
        self.assertEqual((retorna_saque(40)), [20, 20])

    def test_sacar_40_reais(self):
        self.assertEqual((retorna_saque(40)), [20, 20])

    def test_sacar_50_reais(self):
        self.assertEqual((retorna_saque(50)), [50])

    def test_sacar_120_reais(self):
        self.assertEqual((retorna_saque(120)), [100, 20])

    def test_sacar_300_reais(self):
        self.assertEqual((retorna_saque(300)), [100, 100, 100])


    def test_sacar_170_reais(self):
        self.assertEqual((retorna_saque(170)), [100, 50, 20])








if __name__ == "__main__":
    unittest.main()