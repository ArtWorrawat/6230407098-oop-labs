def sum(first, second):
    return first + second

def subtract(first, second):
    return first - second

def mul(first, second):
    return first * second

def divide(first, second):
    if not second == 0:
        return first / second
    else:
        raise ValueError("Fail")