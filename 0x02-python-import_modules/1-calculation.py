#!/usr/bin/python3
def add(a=10, b=5):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    print(f"{a} + {b} = {a + b}")
    return (a + b)


def sub(a=10, b=5):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    print(f"{a} - {b} = {a - b}")
    return (a - b)


def mul(a=10, b=5):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    print(f"{a} * {b} = {a * b}")
    return (a * b)


def div(a=10, b=5):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    print(f"{a} / {b} = {int(a / b)}")
    return int(a / b)
