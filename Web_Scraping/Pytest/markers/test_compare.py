import pytest


@pytest.mark.great
def test_lessthan():
    num = 50
    assert num < 100


@pytest.mark.great
def test_great_equal():
    num = 95
    assert num >= 95


@pytest.mark.others
def test_greaterthan():
    num = 500
    assert num > 400
