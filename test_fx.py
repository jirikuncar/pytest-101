"""Test FX API."""

import fx


def test_convert(cur, data):
    """Check happy convertion path."""
    #: Act
    result = fx.convert(cur, 100, "EUR", "USD")

    #: Assert
    assert result == 125


def test_convert_same_currencies(cur, data):
    """Convert same currencies."""
    #: Act
    result = [fx.convert(cur, 1, symbol, symbol) for symbol in data]

    #: Assert
    assert result == [1, 1]
