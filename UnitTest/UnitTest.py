

import pytest
  
from AddingNumbers import add_numbers

def test_add_positive_numbers():
   
    result = add_numbers(5, 3)
    assert result == 8

def test_add_negative_numbers():
    
    result = add_numbers(-2, -4)
    assert result == -6

def test_add_mixed_numbers():
    
    result = add_numbers(4, -1)
    assert result == 3

def test_add_zero():
    
    result = add_numbers(10, 0)
    assert result == 10
