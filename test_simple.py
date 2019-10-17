"""test_simple.py"""

import pytest


def test_equality_1():
    assert 10 == 10


def test_equality_2():
    assert 10 == int("10")


def test_approx():
    assert .6 / .4 == pytest.approx(1.5)


def test_set():
    assert 6 in set(range(0, 10, 2))
