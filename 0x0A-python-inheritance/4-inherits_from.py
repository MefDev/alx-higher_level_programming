#!/usr/bin/python3
"""a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
; otherwise False."""


def inherits_from(obj, a_class):
    """Check if it inherit from the base class"""
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
