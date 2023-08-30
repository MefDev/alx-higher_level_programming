#!/usr/bin/python3

"""
Square her like crazy
"""


class Square:
    """ create basic class """

    def __init__(self, size=0):
        self.set_size(size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def get_size(self):
        return self.size

    def set_size(self, value):
        self.size = value

    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        else:
            return pow(self.size, 2)
