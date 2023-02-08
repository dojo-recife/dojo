from unittest import TestCase
import unittest
from main import *
import random

class Test(TestCase):
    def test_duas_palavras(self):
        self.assertEqual(quebra_de_linha("Coding dojo", 1), "Coding\ndojo")

    def test_tres_palavras(self):
        self.assertEqual(quebra_de_linha("Coding dojo Recife", 1), "Coding\ndojo\nRecife")

if __name__ == "__main__":
    unittest.main()