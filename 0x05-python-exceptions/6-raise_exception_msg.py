#!/usr/bin/python3
def raise_exception_msg(message=""):
    if (len(message) < 0):
        raise TypeError(message)
    else:
        print(message)
