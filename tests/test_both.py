import pytest
import src.both

def test_both1():
    assert src.both.both(6, 2) == True
    
def test_both2():
    assert src.both.both(0, 0) == True
    
def test_both3():
    assert src.both.both(-1, 2) == False
    
def test_both4():
    assert src.both.both(0, 2) == False
    
