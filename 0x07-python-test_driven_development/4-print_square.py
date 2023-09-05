#!/usr/bin/python3
def print_square(size):
    """ print a square"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        dash = ""
        for i in range(size):
            dash += "#"
        for i in range(size):
            print(dash, end='\n')
