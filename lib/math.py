def addition(a,b):
    return a + b

def subtract(a,b):
    return a -b

def divide(a,b):
    return a/b

def powerOf(a,b):
    return a ** b

def raise_error(user_input:int):
    if user_input < 1:
        raise ValueError(" Sorry, the input must be greater than 2")

