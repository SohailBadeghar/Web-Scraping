import math


def test_smoke_scenario1():
    print("test_case1")


def test_smoke_scenario2():
    print("test_case2")


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def testsquare():
    num = 7
    assert 7*7 == 40


def test_quality():
    assert 10 == 11


class TestDemo():
    def test_inside_class(self):
        print("class inside test case")
