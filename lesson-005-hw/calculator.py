def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0 or a == 0:
        return 'Error: division by zero is not possible!'
    else:
        return a / b
