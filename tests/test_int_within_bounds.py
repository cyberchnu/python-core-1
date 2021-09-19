import pytest
import src.int_within_bounds

def test_int_within_bounds1():
    assert src.int_within_bounds.int_within_bounds(3, 1, 9) == True
    
def test_int_within_bounds2():
    assert src.int_within_bounds.int_within_bounds(6, 1, 6) == False
    
def test_int_within_bounds3():
    assert src.int_within_bounds.int_within_bounds(4.5, 3, 8) == False
    
