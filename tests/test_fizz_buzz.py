import pytest
import src.fizz_buzz

def test_fizz_buzz_3():
    assert src.fizz_buzz.fizz_buzz(6) == "Fizz"
    
def test_fizz_buzz_5():
    assert src.fizz_buzz.fizz_buzz(10) == "Buzz"
    
def test_fizz_buzz_15():
    assert src.fizz_buzz.fizz_buzz(15) == "FizzBuzz"
    
def test_fizz_buzz_7():
    assert src.fizz_buzz.fizz_buzz(7) == "7"
