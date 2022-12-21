# coding: utf-8
import unittest
from cheque import cheque

class TestCheque(unittest.TestCase):
    
    def test_um_real(self):
        self.assertEqual(cheque('um real'), '1.00')

    def test_dois_reais(self):
        self.assertEqual(cheque('dois reais'), '2.00')
    
    def test_dez_reais(self):
        self.assertEqual(cheque('dez reais'), '10.00')

    def test_cinquenta_reais(self):
        self.assertEqual(cheque('cinquenta reais'), '50.00')

    def test_cinquenta_e_tres_reais(self):
        self.assertEqual(cheque('cinquenta e três reais'), '53.00')

    def test_cento_e_cinquenta_e_tres_reais(self):
        self.assertEqual(cheque('cento e cinquenta e três reais'), '153.00')

    def test_dois_milhoes_reais(self):
        self.assertEqual(cheque('dois milhões de reais'), '2000000.00')

if __name__ == '__main__':
    unittest.main()