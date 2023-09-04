#!/usr/bin/python3
def add_integer(a, b=98):
    """ Add two integers """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return int(a) + int(b)
    elif isinstance(a, float) and isinstance(b, int):
        return int(a) + b
    elif isinstance(a, int) and isinstance(b, float):
        return a + int(b)
    elif not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")