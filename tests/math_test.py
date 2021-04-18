#import the pyest framework
import pytest
#import the math file from the lib directory
from lib.math import *

#test the sum function
def test_add():
    result = addition(2,3)
    assert result == 5

#test that the result is 'a' to the power of 'b'
def test_power():
    result = powerOf(2,3)
    assert result == 8

#skip the subtraction test
@pytest.mark.skip()
def test_sub():
    result = subtract(5,1)
    assert result == 4