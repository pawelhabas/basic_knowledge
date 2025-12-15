# Basic usage of unittest framework
#   assert test samples:
#   - Equal
#   - True / False
#   - Raises
#   - Almost Equal
#   - Is None

import unittest


class TestSplitMethod(unittest.TestCase):
    """ assert Equal tests"""

    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'Testing'])

    def test_split_by_comma(self):
        actual = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(actual, expected)

    def test_split_by_hash(self):
        actual = 'summer#time#vibes'.split('#')
        expected = ['summer', 'time', 'vibes']
        self.assertEqual(actual, expected)


from collections import Counter


class TestIsInstance(unittest.TestCase):
    """ assert True / False tests"""

    def test_case_1(self):
        self.assertTrue(isinstance((), tuple))

    def test_case_2(self):
        self.assertTrue(isinstance([], list))
        self.assertFalse(isinstance([], tuple))

    def test_case_3(self):
        self.assertTrue(isinstance({}, dict))
        self.assertFalse(isinstance([], tuple))

    def test_case_4(self):
        cnt = Counter()
        self.assertTrue(isinstance(cnt, Counter))
        self.assertFalse(isinstance(cnt, str))

    def test_case_5(self):
        var1 = 4
        self.assertTrue(isinstance(var1, int))
        self.assertFalse(isinstance(var1, str))

    def test_case_6(self):
        var2 = 4,
        self.assertTrue(isinstance(var2, tuple))
        self.assertFalse(isinstance(var2, list))


###################

class StringReverser:
    def reverse(self, string):
        return string[::-1]


class TestStringReverser(unittest.TestCase):
    """ simple class testing"""

    def test_reverse(self):
        reverser = StringReverser()

        self.assertEqual(reverser.reverse('hello'), 'olleh')
        self.assertEqual(reverser.reverse('12345'), '54321')
        self.assertEqual(reverser.reverse(''), '')


#################

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height


class TestRectangle(unittest.TestCase):
    """ assert Raises tests"""

    def test_area_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 5)

        self.assertRaises(ValueError, Rectangle, [-4, 5])

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

        self.assertRaises(ValueError, Rectangle, [4, -5])


############################

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32


class TestTemperatureConverter(unittest.TestCase):
    """ assert Almost Equal tests"""

    def test_celsius_to_fahrenheit(self):
        tc = TemperatureConverter()
        self.assertAlmostEqual(tc.celsius_to_fahrenheit(-10), 13, delta=2)  # 14

        self.assertAlmostEqual(tc.celsius_to_fahrenheit(0), 32, delta=0.5)

        self.assertAlmostEqual(tc.celsius_to_fahrenheit(15), 59, delta=0.5)


##########################

def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


class TestFindLargest(unittest.TestCase):
    """ assert Is None tests"""

    def test_find_largest_empty_input(self):
        self.assertIsNone(find_largest([]))
