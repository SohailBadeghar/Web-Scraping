
# '''
# In this test cases first function will failed and remaining 2 function will be passed.
# '''
# def test_greater():
#    num = 100
#    assert num > 100

# def test_greater_equal():
#    num = 100
#    assert num >= 100

# def test_less():
#    num = 100
#    assert num < 200



'''
written some addition func and created testcase for that and pass the value and checks wheter test case pas aur fail.
'''
def sum(num1,num2):
   return num1+num2

import pytest

def test_sum():
   assert sum(1,2) == 3



'''
Reverse the string.
'''

def reverse_string(string):
   str = ""
   for i in string:
      rever_str = i + str
   return rever_str


import pytest

def test_reverse_string():
   assert reverse_string("Sohail") == "liahos"