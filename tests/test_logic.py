"""
Unit tests for the number_to_words conversion logic.

These tests ensure that the core conversion logic behaves correctly
for common cases and edge cases.
"""

from ntow.logic import number_to_words


def test_zero():
    """Zero should be converted explicitly."""
    assert number_to_words(0) == "zero"


def test_single_digit():
    """Single digit numbers should convert correctly."""
    assert number_to_words(7) == "seven"
