import unittest
from main import *


class TestName(unittest.TestCase):
    """
    local onde é adicionado os testes como o do exemplo abaixo:
        ex:
            def test_example(self):
                self.assertEqual(module(arg), expected_result)
    """
    def test_example(self):
        self.assertEqual(function(), None)


if __name__ == '__main__':
    unittest.main()
