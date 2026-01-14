# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.
#
# Task:
# - Input: "small", "medium", "large"
# - Small -> 10$, Medium -> 15$, Large -> 20$
# - If invalid: show "Unknown cup size"
import unittest
from unittest.mock import patch


def tea_stall() -> str:
    tea_prices = {'small': 10, 'medium': 15, 'large': 20}
    chosen_size = input("Choose your cup size (small/medium/large): ")
    if type(chosen_size) is not str or chosen_size.lower().strip() not in tea_prices.keys():
        return 'Unknown cup size'
    return "Price is {}$".format(tea_prices[chosen_size.lower().strip()])


class TestTeaStall(unittest.TestCase):

    @patch("builtins.input", return_value="")
    def test_tea_stall_empty(self, mocked_size):
        self.assertEqual(tea_stall(), 'Unknown cup size')

    @patch("builtins.input", return_value="extra large")
    def test_tea_stall_wrong_size(self, mocked_size):
        self.assertEqual(tea_stall(), 'Unknown cup size')

    @patch("builtins.input", return_value=5)
    def test_tea_stall_number(self, mocked_size):
        self.assertEqual(tea_stall(), 'Unknown cup size')

    @patch("builtins.input", return_value=None)
    def test_tea_stall_none(self, mocked_size):
        self.assertEqual(tea_stall(), 'Unknown cup size')

    @patch("builtins.input", return_value=False)
    def test_tea_stall_false(self, mocked_size):
        self.assertEqual(tea_stall(), 'Unknown cup size')

    @patch("builtins.input", return_value="small")
    def test_tea_stall_small(self, mocked_size):
        self.assertIn('10$', tea_stall())

    @patch("builtins.input", return_value="medium")
    def test_tea_stall_medium(self, mocked_size):
        self.assertIn('15$', tea_stall())

    @patch("builtins.input", return_value="large")
    def test_tea_stall_large(self, mocked_size):
        self.assertIn('20$', tea_stall())
