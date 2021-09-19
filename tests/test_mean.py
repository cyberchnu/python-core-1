import pytest
import src.mean

def test_mean1():
    assert src.mean.mean(42) == 3
    
def test_mean2():
    assert src.mean.mean(12345) == 3
    
def test_mean3():
    assert src.mean.mean(666) == 6
    
