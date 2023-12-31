#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A class to json using dict"""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return ({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if (json):
            self.__dict__ = json
