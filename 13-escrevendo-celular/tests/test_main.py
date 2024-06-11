"""
Letras  ->  Número 
ABC    ->  2 
DEF    ->  3 
GHI    ->  4 
JKL    ->  5 
MNO    ->  6 
PQRS   ->  7 
TUV    ->  8 
WXYZ   ->  9 
Espaço -> 0 
"""

from main import generic_function

def test_one_letter():
    output = generic_function("a")
    assert output == "2"

def test_j():
    output = generic_function("j")
    assert output == "5"


def test_b():
    output = generic_function("b")
    assert output == "22"

def test_oi():
    output = generic_function("oi")
    assert output == "666444"

def test_espaco():
    output = generic_function(" ")
    assert output == "0"

def test_palavra_com_espaco():
    output = generic_function("dojo recife")
    assert output == "36665666077733222444333_33"

def test_final():
    output = generic_function("SEMPRE ACESSO O DOJOPUZZLES")
    assert output == "77773367_7773302_222337777_777766606660366656667889999_9999555337777"



