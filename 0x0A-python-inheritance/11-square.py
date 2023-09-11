#!/usr/bin/python3
"""class square (based on 9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates a sqaure class"""

    def __init__(self, size):
        """initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Print the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
