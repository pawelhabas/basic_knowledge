# assert
#   in Python is a statement used to verify assumptions during program execution
#   — if the condition is false, the program stops and raises an AssertionError.
#   It is most often used during debugging to quickly detect unexpected states.
#   DO NOT USE ON PROD

# 1. Validating function arguments during debugging

def divide(a, b):
    assert b != 0, "Denominator must not be zero"
    return a / b


# 2. Checking the types of sensitive data (e.g., input from external sources)

def process(items):
    assert isinstance(items, list), "Expected a list"
    pass


# 3. Verifying logical assumptions in algorithms

def find_min(values):
    assert len(values) > 0, "Values cannot be empty"
    return min(values)


# 4. Checking an object's state after an operation
class SomeObject:
    is_ready = False

    def initialize(self):
        pass


obj = SomeObject()
obj.initialize()
assert obj.is_ready, "Object should be ready after initialization"


# 5. Auxiliary testing during implementation
def compute_something():
    return True


result = compute_something()
assert result >= 0, "Result must be non-negative"


# 6. Checking data types

def dodaj(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    return a + b


# 7. Validating function arguments

def ustaw_wiek(wiek):
    assert 0 <= wiek <= 120, "Wiek wygląda podejrzanie"
    return wiek


# 8. Controlling application state during debugging

lista = [1, 2, 3]
lista.pop()
assert len(lista) == 2


# 9. Checking invariants in classes

class Konto:
    def __init__(self, saldo):
        self.saldo = saldo
        assert self.saldo >= 0


# 10. Ensuring that a function returns meaningful data

def policz():
    wynik = 42
    assert wynik is not None
    return wynik


####################
#
#   Examples v2
#
####################

# 1. Simple value check
x = 10
assert x > 0, "x must be positive"


# 2. Validating function arguments
def divide(a, b):
    assert b != 0, "b cannot be zero"
    return a / b


# 3. Ensuring expected list contents
items = [1, 2, 3]
assert len(items) == 3, "List length is incorrect"

# 4. Checking type assumptions
name = "Alice"
assert isinstance(name, str), "name must be a string"


# 5. Validating intermediate computation
def some_function():
    return True


result = some_function()
assert result is not None, "Function returned None unexpectedly"

####################
#
#   Other examples
#
####################


try:
    def divide(a, b):
        assert b != 0, "Division by zero is not allowed!"
        return a / b


    print(divide(10, 2))  # No assertion error
    print(divide(10, 0))  # Raises AssertionError with the message

except Exception as e:
    print(type(e), e)

########
try:
    countries = ['POL', 'ENG', 'GER', 'USA', 'IsTA']
    is_italy = 'ITA' in countries

    assert is_italy, "Italy not found in the countries list."

except Exception as e:
    print(type(e), e)
########
try:
    def max_min_diff(numbers):
        """
        Calculates the difference between the maximum and minimum number
        in the given list.

        :param numbers: A list of numbers.
        :return: The difference between the maximum and minimum number
        in the list.
        :raises ValueError: If the list is empty.
        """
        assert len(numbers) != 0
        return max(numbers) - min(numbers)


    print(max_min_diff([1, ]))
    print(max_min_diff([]))

except Exception as e:
    print(type(e), e)
########
try:
    from typing import Union


    def max_min_diff(numbers: list) -> Union[int, float]:  # dla python 3.8, 3.9
        # def max_min_diff(numbers: list) -> int | float:   # dla python 3.10+
        """
        Calculates the difference between the maximum and minimum number
        in the given list.

        :param numbers: A list of numbers.
        :return: The difference between the maximum and minimum number
        in the list.
        :raises ValueError: If the list is empty.
        """
        assert len(numbers) != 0, 'The input list cannot be empty.'
        return max(numbers) - min(numbers)


    print(max_min_diff([1, ]))
    print(max_min_diff([]))
except Exception as e:
    print(type(e), e)
########
try:
    def rectangle_area(width: int, height: int) -> int:
        """
        Calculates the area of a rectangle with given width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: The area of the rectangle.
        :raises TypeError: If the width or height is not an integer.
        :raises ValueError: If the width or height is not a positive integer.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError('The width and height must be integers.')
        if width <= 0 or height <= 0:
            raise ValueError(
                'The width and height must be positive integers.'
            )
        return width * height


    assert rectangle_area('5', '4') == 20
except Exception as e:
    print(type(e), e)
########
try:
    def rectangle_area(width: int, height: int) -> int:
        """
        Calculates the area of a rectangle with given width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: The area of the rectangle.
        :raises TypeError: If the width or height is not an integer.
        :raises ValueError: If the width or height is not a positive integer.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError('The width and height must be integers.')
        if width <= 0 or height <= 0:
            raise ValueError(
                'The width and height must be positive integers.'
            )
        return width * height


    assert rectangle_area(-4, 5) == 20
except Exception as e:
    print(type(e), e)
########
try:
    def calculate_income_tax(
            amount: float, tax_rate: float, age: int
    ) -> int:
        """
        Calculates the income tax based on the given amount, tax rate,
        and age.

        :param amount: The amount of income.
        :param tax_rate: The tax rate as a decimal.
        :param age: The age of the taxpayer.
        :return: The amount of income tax.
        """
        if age <= 18:
            return int(min(amount * tax_rate, 5000))
        elif age <= 65:
            return int(amount * tax_rate)
        else:
            return int(min(amount * tax_rate, 8000))


    def test_calculate_income_tax():
        assert calculate_income_tax(60000, 0.15, 10) == 50000, 'test_calculate_income_tax1'
        assert calculate_income_tax(60000, 0.15, 18) == 50000, 'test_calculate_income_tax2'
        assert calculate_income_tax(60000, 0.15, 19) == 90000, 'test_calculate_income_tax3'
        assert calculate_income_tax(60000, 0.15, 65) == 90000, 'test_calculate_income_tax4'
        assert calculate_income_tax(60000, 0.15, 66) == 80000, 'test_calculate_income_tax5'


    test_calculate_income_tax()
except Exception as e:
    print(type(e), e)
########
try:
    def factorial(n: int) -> int:
        """
        Calculates the factorial of a positive integer.

        :param n: The integer to calculate the factorial of.
        :return: The factorial of the integer.
        :raises ValueError: If the integer is negative.
        """
        if n < 0:
            raise ValueError(
                'Cannot calculate factorial of a negative number.'
            )
        elif n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
        assert False
    except ValueError:
        print('ValueError')
except Exception as e:
    print(type(e), e)
########
try:
    def calculate_median(numbers: list) -> float:
        """
        Calculates the median value of the given list of numbers.

        :param numbers: The list of numbers.
        :return: The median value.
        :raises ValueError: If the list is empty.
        """
        if not numbers:
            raise ValueError("List is empty")
        sorted_nums = sorted(numbers)
        length = len(sorted_nums)

        if length % 2 == 0:
            return (
                    sorted_nums[length // 2 - 1] + sorted_nums[length // 2]
            ) / 2
        else:
            return sorted_nums[length // 2]


    def test_calculate_median():
        assert calculate_median([1, 2, 3]) == 2
        assert calculate_median([4, 5, 6, 7]) == 5.5
        assert calculate_median([2, 1, 3]) == 2
        assert calculate_median([0, 0, 0, 0]) == 1, 'error1'
        try:
            calculate_median([])
            assert False
        except ValueError:
            pass


    test_calculate_median()
except Exception as e:
    print(type(e), e)
########
try:
    pass
except Exception as e:
    print(type(e), e)
