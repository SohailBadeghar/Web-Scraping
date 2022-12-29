import pytest
import math


'''
These are custom markers which we have created in this file.
'''


@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


@pytest.mark.square
def testsquare():
    num = 7
    assert 7*num == 49


@pytest.mark.others
def test_equality():
    assert 10 == 11


'''
These are the built in Marker is used .
'''


@pytest.mark.skip
def test_skip():
    a = 4
    assert a*2 == 4


@pytest.mark.xfail
def test_checkdatatype():
    a = 5
    assert type(a) == int


'''
Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker.

'''

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output