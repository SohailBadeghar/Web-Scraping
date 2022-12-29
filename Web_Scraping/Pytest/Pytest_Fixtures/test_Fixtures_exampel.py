import pytest

@pytest.fixture()
def numbers():
    a,b,c = 15,20,30
    return [a,b,c]


@pytest.mark.xfail
def test_method1(numbers):
        x = 10
        assert numbers[0] == x

@pytest.mark.skip
def test_method2(numbers):
        y = 20
        assert numbers[1] == y

def test_method3(numbers):
        z = 30
        assert numbers[2] == z