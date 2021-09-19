import pytest
import src.hello

def test_hello():
    assert src.hello.hello() == "Hello!"
