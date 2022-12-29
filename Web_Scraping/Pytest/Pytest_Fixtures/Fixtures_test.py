import pytest

'''
we can use Fixtures within File and check here are the example.
'''

'''
This is my one method fixture wriiten below:
'''
@pytest.fixture
def input_value():
    input = 30
    return input

'''
Using the fixture written some methods.
'''

def test_fixture_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_fixture_multiply_by_3(input_value):
    assert input_value * 3 == 90





'''
Here we can reuse the one fixture into another fixtures to execute some operation , The fixture are resuble.
if we get bug in one of the fixture it raise the exception error and test case will be failed.
'''

@pytest.fixture
def order():
    return []


@pytest.fixture
def append_first(order):
    order.append(1)


@pytest.fixture
def append_second(order, append_first):
    order.extend([2])


@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [3]


def test_order(order):
    assert order == [1, 2, 3]