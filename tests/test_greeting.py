import pytest
from lib.greeting import greeting

def test_greeting():
    greet = greeting("Charlie")
    assert greet == "Hello, Charlie."