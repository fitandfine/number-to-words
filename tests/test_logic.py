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
def test_teens():
    """Teen numbers (10–19) are special cases in English."""
    assert number_to_words(13) == "thirteen"


def test_tens():
    """Multiples of ten should be converted properly."""
    assert number_to_words(40) == "forty"


def test_hundreds():
    """Numbers in the hundreds should include 'hundred'."""
    assert number_to_words(215) == "two hundred fifteen"


def test_thousands():
    """Thousand-level numbers should include 'thousand'."""
    assert number_to_words(1001) == "one thousand one"


def test_millions():
    """Million-level numbers should be supported."""
    assert number_to_words(1_000_001) == "one million one"


def test_billions():
    """Billion-level numbers should be supported."""
    assert number_to_words(1_000_000_000) == "one billion"


def test_trillions():
    """Trillion-level numbers should be supported."""
    assert number_to_words(1_000_000_000_000) == "one trillion"