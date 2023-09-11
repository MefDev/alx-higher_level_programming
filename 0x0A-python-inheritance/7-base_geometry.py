#!/usr/bin/python3

class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """AREA BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validation BaseGeometry"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
