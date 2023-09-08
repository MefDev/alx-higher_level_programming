#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Real definition of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculate the areas."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter."""
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if not self.perimeter():
            return ""
        return '\n'.join(["{}".format(self.print_symbol) *
                          self.width for _ in range(self.height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        elif not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return rect_2

    @staticmethod
    def square(cls, size=0):
        return cls(size, size)
