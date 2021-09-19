import pytest
import src.sum_even_nums_in_range

def test_sum_even_nums_in_range1():
    assert src.sum_even_nums_in_range.sum_even_nums_in_range(10, 20) == 90
    
def test_sum_even_nums_in_range2():
    assert src.sum_even_nums_in_range.sum_even_nums_in_range(51, 150) == 5050
    
def test_sum_even_nums_in_range3():
    assert src.sum_even_nums_in_range.sum_even_nums_in_range(63, 97) == 1360
    
