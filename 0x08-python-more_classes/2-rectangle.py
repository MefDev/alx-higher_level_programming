#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Real definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the data."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the data to a new value."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Retrieve the data."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the data to a new value."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def area(self):
        """Calculate the areas."""
        return self.__height * self.__width

    @property
    def perimeter(self):
        """Calculate the perimeter."""
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)
