import pytest
import src.tri_area

def test_tri_area1():
    assert src.tri_area.tri_area(3, 2) == 3
    
def test_tri_area2():
    assert src.tri_area.tri_area(7, 4) == 14
    
def test_tri_area3():
    assert src.tri_area.tri_area(10, 10) == 50
    
