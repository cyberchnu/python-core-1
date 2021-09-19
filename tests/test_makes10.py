import pytest
import src.makes10

def test_makes10_1():
    assert src.makes10.makes10(9, 10) == True
    
def test_makes10_2():
    assert src.makes10.makes10(9, 9) == False
    
def test_makes10_3():
    assert src.makes10.makes10(1, 9) == True
    
