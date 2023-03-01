from unittest import TestCase
import unittest
from main import *
import random

# entrada: lista de mictorios
# saida: lista de mictorios disponiveis respeitando as regras
# de adjacencia.

class Test(TestCase):
    def test_mictorio_simples(self):
        self.assertEqual(mictorio([0]), [0])

        
    def test_mictorio_tres(self):
        self.assertEqual(
            mictorio([0, 0, 0]), [0, 2]
        )

    def test_mictorio_tres_livres_um_ocupado(self):
        self.assertEqual(
            mictorio([1, 0, 0]), [2]
        )

    def test_mictorio_tres_livres_meio_ocupado(self):
        self.assertEqual(
            mictorio([0, 1 , 0]), []
        )        

if __name__ == "__main__":
    unittest.main()