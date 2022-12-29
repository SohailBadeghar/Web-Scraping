import pytest
import math

'''
In this functions we are checking the conditions and how many test cases are going to fail.
after failed some conditions the we have to stop the execution.
"/pytest -vs filename --maxfail (count)/"
using this cmd you can stop execution after some condition fails.
'''

def test_prod_failure():
   num =(2,2,2)
   assert math.prod(num) == 4

def test_capitalize_failure():
   string = "sohail"
   assert string.capitalize() == "SOHAIL"

def test_len_failure():
   a="Neosoft"
   b= "Great"
   assert len(b) == len(a)