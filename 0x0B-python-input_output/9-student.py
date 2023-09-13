#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A class to json using dict"""
        return self.__dict__
