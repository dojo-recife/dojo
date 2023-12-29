import unittest
from main import numeros_na_linha
# 


class TestCase(unittest.TestCase):

    def test_duas_strings(self):
        numero = numeros_na_linha("onetwo")
        self.assertEqual(numero, "12")
    
    def test_duas_strings_com_caractere_separador(self):
        numero = numeros_na_linha("two$two")
        self.assertEqual(numero, "22")
    
    def test_apenas_int(self):
        numero = numeros_na_linha("1234")
        self.assertEqual(numero, "14")
    
    def test_apenas_int_2(self):
        numero = numeros_na_linha("123458")
        self.assertEqual(numero, "18")
    
    def test_int_and_str(self):
        numero = numeros_na_linha("12a345")
        self.assertEqual(numero, "15")
    
    def test_int_and_pipe_and_int(self):
        numero = numeros_na_linha("12|345")
        self.assertEqual(numero, "15")
    
    def test_str_and_number(self):
        numero = numeros_na_linha("one5")
        self.assertEqual(numero, "15")
    
    def test_first_str_and_number_2(self):
        numero = numeros_na_linha("xtwoone3four")
        self.assertEqual(numero, "24")

    def test_str_and_number_3(self):
        numero = numeros_na_linha("twoone3fourx")
        self.assertEqual(numero, "24")
    
    def test_str_and_number_4(self):
        numero = numeros_na_linha("twone3furx")
        self.assertEqual(numero, "23")
        
    def test_treb7uchet(self):
        num = numeros_na_linha("treb7uchet")
        self.assertEqual(num, "77")
        
    
        

       
# twone3fourx
# xtwone3fourx
# 

if __name__ == "__main__":
    unittest.main()