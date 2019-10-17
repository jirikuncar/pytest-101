"""Validate raised exceptions."""

import pytest


def test_value_error():
    with pytest.raises(ZeroDivisionError) as context:
        1/0

    assert str(context.value) == "division by zero"
