import pytest


'''
This fixture has function scope and also if we didn't mentioned any scope it takes default function scope.
'''

class Test:

    @pytest.fixture(scope='function', autouse=True )  #autouse=true means  it will call automataically berfore each function.
    def myfixture(self):
        print("my fixture is called ")

    def test_method1(self):
        print("method-1 is called")

    def test_method2(self):
        print("method-2 is called")


'''
class scope.
'''
class Test2:

    @pytest.fixture(scope='class', autouse=True )  #autouse=true means  it will call automataically berfore each function.
    def myfixture(self):
        print("my fixture is called ")

    def test_method1(self):
        print("method-1 is called")

    def test_method2(self):
        print("method-2 is called")
