#import the pyest framework
import pytest
#import the math file from the lib directory
from lib.math import *

@pytest.fixture
def input():
    return(12)

#test the sum function
def test_add(input):
    result = addition(input,3)
    assert result == 15

#test that the result is 'a' to the power of 'b'
def test_power(input):
    result = powerOf(input,3)
    assert result == 1728

#skip the subtraction test
@pytest.mark.skip()
def test_sub():
    result = subtract(5,1)
    assert result == 4