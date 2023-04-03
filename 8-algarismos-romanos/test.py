import unittest
from main import numeros_arabicos_romanos, numeros_romanos_arabicos

class TestCase(unittest.TestCase):

    def test_um_arabico(self):
        result = numeros_arabicos_romanos(1)
        self.assertEqual(result, "I")
        
    def test_cinco_arabico(self):
        result = numeros_arabicos_romanos(5)
        self.assertEqual(result, "V")

    def test_dez_arabico(self):
        result = numeros_arabicos_romanos(10)
        self.assertEqual(result, "X")

    def test_um_romano(self):
        result = numeros_romanos_arabicos("I")
        self.assertEqual(result, 1)
        
    def test_trezentos_romano(self):
        result = numeros_romanos_arabicos("CCC")
        self.assertEqual(result, 300)

    def test_trinta_romano(self):
        result = numeros_romanos_arabicos("XXX")
        self.assertEqual(result, 30)

    def test_trinta_arabico(self):
        result = numeros_arabicos_romanos(30)
        self.assertEqual(result, "XXX")
        
    def test_dois_mil_arabico(self):
        result = numeros_arabicos_romanos(2000)
        self.assertEqual(result, "MM")
    
    def test_seis_romano(self):
        result = numeros_romanos_arabicos("VI")
        self.assertEqual(result, 6)
        
    def test_seis_arabico(self):
        result = numeros_arabicos_romanos(6)
        self.assertEqual(result, "VI")

if __name__ == "__main__":
    unittest.main()