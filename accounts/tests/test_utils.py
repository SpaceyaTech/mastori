"""
Tests for helpers and utilities for the `mastori::accounts` app.  

Note:
    Prefer to inherit from `unittest` for util functions or services.
    This reduces the DB overhead of using `django.test.TestCase`. 
    Consider a different design approach if you find your utilities
    dependent on DB transactions.
"""

import secrets
import unittest
from unittest.mock import call, patch

from accounts.models import generate_verification_code


BASE_MODULE: str = "accounts.models"


def _mock_choice_response(sequence: str, calls: int = 1) -> list[int]:
    """
    Test helper to mock and simulate `secrets.choice` func calls.
    """
    assert isinstance(sequence, str)
    return [secrets.choice(sequence) for _ in range(calls)]


class VerificationCodeTestCase(unittest.TestCase):
    """
    Tests to cover generating verification codes for the `user` model.
    """

    def setUp(self) -> None:
        return super().setUp()

    def test_should_raise_exc_for_out_of_range_code_size_arg(self) -> None:
        # Given
        invalid_lengths = (3, 12, -1)

        for length in invalid_lengths:
            # Then
            with self.assertRaises(ValueError):
                generate_verification_code(size=length)  # When

    def test_should_securely_generate_user_verification_code(self) -> None:
        # Given
        length = 6
        sequence = "0123456789"
        choice_side_effect = _mock_choice_response(sequence, length)
        expected = "".join(choice_side_effect)

        # When
        with patch(f"{BASE_MODULE}.secrets", autospec=True) as mock_secrets_lib:
            mock_secrets_lib.choice.side_effect = choice_side_effect
            actual = generate_verification_code(size=length)

        # Then
        mock_secrets_lib.choice.assert_has_calls([call(sequence)] * length)
        self.assertIsInstance(actual, str)
        self.assertEqual(mock_secrets_lib.choice.call_count, length)
        self.assertEqual(actual, expected)
