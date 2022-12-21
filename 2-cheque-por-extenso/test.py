# Este problema foi utilizado em 1308 Dojo(s).
#
# Apesar de o volume de cheques emitidos tenha diminuído drásticamente nos últimos anos, principalmente devido a popularização dos cartões de crédito e débito, eles ainda são utilizados em muitas compras, especialmente a de valores altos. E para auxiliar no seu preenchimento, vários estabelecimentos possuem máquinas que dado o valor da compra, preenchem o cheque com o seu valor por extenso.
#
# Desenvolva um programa que dado um valor monetário, seja retornado o valor em reais por extenso.
#
# Exemplo:
#
# 15415,16 -> quinze mil quatrocentos e quinze reais e dezesseis centavos
# 0,05 -> cinco centavos
# 2,25 -> dois reais e vinte e cinco centavos
# https://dojopuzzles.com/problems/cheque-por-extenso/

from unittest import TestCase
import unittest
from main import *
import random
class Test(TestCase):
    def test_um(self):
        self.assertEqual(cheque(1),"um")
    def test_dois(self):
        self.assertEqual(cheque(2),"dois")

    def test_nove(self):
        self.assertEqual(cheque(9), "nove")

    def test_numero_com_1_digito(self):
        lista = ["um","dois","tres","quatro","cinco","seis","sete","oito","nove"]

        for i in range(1, 10):
            self.assertEqual(cheque(i), lista[i - 1])

    def test_numero_com_2_digitos(self):
        lista = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

        # 1

        for i in range(10,20):
            n = i % 10
            self.assertEqual(cheque(i), lista[n])

    def test_numero_com_maior_20(self):


        self.assertEqual(cheque(22), "vinte e dois")










if __name__ == "__main__":
    unittest.main()