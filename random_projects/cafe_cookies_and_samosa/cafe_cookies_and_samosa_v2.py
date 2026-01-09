# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosas, it confirms the order.
# Otherwise, it says it's not available.
#
# Task:
# - Take snack input
# - If it's "cookies" or "samosa", confirm the order
# - Else, show unavailability

import unittest
from unittest.mock import patch

from enum import Enum


class OrderReplies(Enum):
    confirmation = 'Order confirmed.'
    unavailability = 'Product unavailable'


def cafe_worker() -> OrderReplies:
    order = input("What will be the order: ")
    return OrderReplies.confirmation if order in ['cookies', 'samosa'] else OrderReplies.unavailability


def test_cafe_worker(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "cookies")
    assert cafe_worker() == OrderReplies.confirmation, 'cookies Failed'

    monkeypatch.setattr("builtins.input", lambda _: "samosa")
    assert cafe_worker() == OrderReplies.confirmation, 'samosa Failed'

    monkeypatch.setattr("builtins.input", lambda _: "cookie")
    assert cafe_worker() == OrderReplies.unavailability, 'cookie Failed'

    monkeypatch.setattr("builtins.input", lambda _: "")
    assert cafe_worker() == OrderReplies.unavailability, 'EmptyString Failed'


class TestCafeWorker(unittest.TestCase):
    @patch("builtins.input", return_value="cookies")
    def test_cafe_worker_confirmation_cookies(self, mock_snack):
        self.assertEqual(cafe_worker(), OrderReplies.confirmation, '"cookies" test Failed')

    @patch("builtins.input", return_value="samosa")
    def test_cafe_worker_confirmation_samosa(self, mock_snack):
        self.assertEqual(cafe_worker(), OrderReplies.confirmation, '"samosa" test Failed')

    @patch("builtins.input", return_value="")
    def test_cafe_worker_unavailability_empty_string(self, mock_snack):
        self.assertEqual(cafe_worker(), OrderReplies.unavailability, 'EmptyString test Failed')

    @patch("builtins.input", return_value="cookie")
    def test_cafe_worker_unavailability_wrong_word_cookie(self, mock_snack):
        self.assertEqual(cafe_worker(), OrderReplies.unavailability, 'Wrong word test Failed')

    @patch("builtins.input", return_value="samosas")
    def test_cafe_worker_unavailability_wrong_word_samosas(self, mock_snack):
        self.assertEqual(cafe_worker(), OrderReplies.unavailability, 'Wrong word test Failed')
