import unittest
from main import maior_q_ou_igual_acinco,produto_matriz


class TestCase(unittest.TestCase):

    def test_n_igual_maior_que_cinco(self):
        maior_que_igual_5 = maior_q_ou_igual_acinco([1, 2, 3, 4, 5])
        self.assertEqual(maior_que_igual_5, True)
        
    def test_n_menor_que_cinco(self):
        maior_que_igual_5 = maior_q_ou_igual_acinco([1, 2])
        
        self.assertEqual(maior_que_igual_5, False)
        
    def test_produto_vetor_de_1(self):
        acumulador=produto_matriz([1,1,1,1,1])          
        self.assertEqual(acumulador,1)
    
    def test_produto_vetor_de_2(self):
        acumulador = produto_matriz([2, 2, 2, 2, 2])
        self.assertEqual(acumulador, 32)
        
    def test_produto_vetor_de_dez_elementos(self):
        acumulador = produto_matriz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(acumulador, 3628800)
    
    def test_produto_vetor_lista_de_lista(self):
        matriz = [
            [2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1]
        ]
        acumulador = produto_matriz(matriz)
    
    
        
if __name__ == "__main__":
    unittest.main()
    #escrever as diagonais