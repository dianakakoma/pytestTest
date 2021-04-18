import pytest
from lib.greeting import greeting

class TestGreeting:
    
    def test_greeting(self):
        greet = greeting("Charlie")
        assert greet == "Hello, Charlie."