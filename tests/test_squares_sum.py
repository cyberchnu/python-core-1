import pytest
import src.squares_sum

def test_squares_sum1():
    assert src.squares_sum.squares_sum(3) == 14
    
def test_squares_sum2():
    assert src.squares_sum.squares_sum(12) == 650
    
def test_squares_sum3():
    assert src.squares_sum.squares_sum(13) == 819
    
