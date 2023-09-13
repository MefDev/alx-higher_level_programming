#!/usr/bin/python3
""" function tha return the dictionary description
with simple data structure"""


def class_to_json(obj):
    """class to json"""
    return obj.__dict__
