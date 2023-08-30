#!/usr/bin/python3

"""
Square her like crazy
"""


class Square:
    """ create basic class """

    def __init__(self, size=0):
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def get_size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return pow(self.size, 2)
