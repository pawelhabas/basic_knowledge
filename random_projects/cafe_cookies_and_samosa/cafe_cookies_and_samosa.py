# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosas, it confirms the order.
# Otherwise, it says it's not available.
#
# Task:
# - Take snack input
# - If it's "cookies" or "samosa", confirm the order
# - Else, show unavailability

import unittest
import pytest
from enum import Enum


class OrderReplies(Enum):
    confirmation = 'Order confirmed.'
    unavailability = 'Product unavailable'


def cafe_worker(order: str) -> OrderReplies:
    return OrderReplies.confirmation if order.strip().lower() in ['cookies', 'samosa'] else OrderReplies.unavailability


def run():
    order = input("What will be the order: ")
    answer = cafe_worker(order).value
    return print(answer)


def test_cafe_worker():
    assert cafe_worker('cookie') == OrderReplies.unavailability, 'cookie Failed'
    assert cafe_worker('cookies') == OrderReplies.confirmation, 'cookies Failed'
    assert cafe_worker('samosa') == OrderReplies.confirmation, 'samosa Failed'
    assert cafe_worker('') == OrderReplies.unavailability, 'empty string Failed'
    with pytest.raises(TypeError):
        cafe_worker()


class TestCafeWorker(unittest.TestCase):
    def test_cafe_worker_confirmation(self):
        self.assertEqual(cafe_worker('cookies'), OrderReplies.confirmation, '"cookies" test Failed')
        self.assertEqual(cafe_worker('samosa'), OrderReplies.confirmation, '"samosa" test Failed')

    def test_cafe_worker_unavailability(self):
        self.assertRaises(TypeError, cafe_worker, )
        self.assertEqual(cafe_worker(''), OrderReplies.unavailability, 'EmptyString test Failed')
        self.assertEqual(cafe_worker('cookie'), OrderReplies.unavailability, 'Wrong word test Failed')
        self.assertEqual(cafe_worker('samosas'), OrderReplies.unavailability, 'Wrong word test Failed')


if __name__ == '__main__':
    run()
