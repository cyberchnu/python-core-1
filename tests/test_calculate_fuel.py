import pytest
import src.calculate_fuel

def test_calculate_fuel1():
    assert src.calculate_fuel.calculate_fuel(15) == 150
    
def test_calculate_fuel2():
    assert src.calculate_fuel.calculate_fuel(23.5) == 235
    
def test_calculate_fuel3():
    assert src.calculate_fuel.calculate_fuel(3) == 100
    
