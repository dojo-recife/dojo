import unittest
from main import conta_buraco

# Buracos nas Letras
# Se você pensar em um papel como um plano e uma letra como uma marcação neste plano, então estas letras dividem o plano em regiões. Por exemplo, as letras A, D e O dividem o plano em 2 pois possuem um espaço confinado em seu desenho, ou um “buraco”. Outras letras como B possuem 2 buracos e letras como C e E não possuem buracos.

# Deste modo podemos considerar que o número de buracos em um texto é igual a soma dos buracos nas palavras dele.

# A sua tarefa é, dado um texto qualquer, encontre a quantidade de buracos nele. 


class TestCase(unittest.TestCase):
    def test_um_caractere_com_buraco(self):
        buracos = conta_buraco("A")
        self.assertEqual(buracos, 1)

    def test_caractere_b_maiusculo_com_buraco(self):
        buracos = conta_buraco("B")
        self.assertEqual(buracos, 2)
        
    def test_caractere_b_minusculo_com_buraco(self):
        buracos = conta_buraco("b")
        self.assertEqual(buracos, 1)

    def test_caractere_sem_buraco(self):
        buracos = conta_buraco("C")
        self.assertEqual(buracos, 0)

    def test_dois_caracteres_sem_buraco(self):
        buracos = conta_buraco("CC")
        self.assertEqual(buracos, 0)
        
    def test_dois_caracteres_com_um_buraco(self):
        buracos = conta_buraco("CD")
        self.assertEqual(buracos, 1)
    
    def test_caractere_P_maiusculo(self):
        buracos = conta_buraco("P")
        self.assertEqual(buracos, 1)
    
    def test_todos_caracteres_com_1_buraco(self):
        buracos = conta_buraco("ADOPQRabdegopq")
        self.assertEqual(buracos, 14)

    def test_todos_caracteres_como_B(self):
        buracos = conta_buraco("BBBBB")
        self.assertEqual(buracos, 10)

    def test_todos_caracteres_como_B(self):
        buracos = conta_buraco("Buraco")
        self.assertEqual(buracos, 4)

    def test_muitos_caracteres(self):
        buracos = conta_buraco("Prazer em te conhecer")
        self.assertEqual(buracos, 8)

    def test_todos_caracteres_como_B(self):
        buracos = conta_buraco("          ")
        self.assertEqual(buracos, 0)



if __name__ == "__main__":
    unittest.main()