import pytest
import src.addition

def test_addition_poz():
    assert src.addition.addition(3, 2) == 5
    
def test_addition_poz_neg():
    assert src.addition.addition(3, -5) == -2
    
def test_addition_neg():
    assert src.addition.addition(-3, -2) == -5
    
def test_addition_zero():
    assert src.addition.addition(3, 0) == 3
