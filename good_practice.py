# Well-defined function
from sympy import false


def add_numbers(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers and return their sum.

    :param a: First number to add
    :param b: Second number to add
    :return: The numerical sum of a and b
    """
    return a + b


#####

#   Unit tests for above function

import unittest

class TestAddNumbers(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_floats(self):
        # when adding floats precision errors may occur
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=7)

    def test_negative_values(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-3, 3), 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            add_numbers("1", 2)
        with self.assertRaises(TypeError):
            add_numbers(false, 2)

if __name__ == '__main__':
    unittest.main()


