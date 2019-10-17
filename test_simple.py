"""test_simple.py"""


def test_equality_1():
    assert 10 == 10


def test_equality_2():
    assert 10 == "10"


def test_approx():
    assert .6 / .4 == 1.5


def test_set():
    assert 6 in {0, 2, 4, 5, 8}
