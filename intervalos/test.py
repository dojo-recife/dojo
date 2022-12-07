import unittest
from main import intervals

class TestCase(unittest.TestCase):

    def test_simple_list(self):
        result = intervals([100, 101])
        self.assertEqual(result, [[100,101]])

    def test_three_numbers(self):
        result = intervals([1, 2, 3])
        self.assertEqual(result, [[1, 3]])

    def test_no_sequence(self):
        result = intervals([1,2,3,5,6])
        self.assertEqual(result, [[1,3], [5,6]])



if __name__ == "__main__":
    unittest.main()