import pytest


def test_subtract():
    a = 5
    b = 5
    assert a - b == 0


def test_divide():
    a = 3
    b = 3
    assert a / b == 1


def multiply():
    a = 3
    b = 4
    assert a * b == 12


def test_multiply():
    a = 6
    b = 6
    assert a * b == 36


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr("X", "check")
