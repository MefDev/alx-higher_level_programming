#!/usr/bin/python3
"""class BaseGeometry (based on 7-base_geometry.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("width", height):
            self.__height = height

        def __str__(self):
            return f"Rectangle(width={self.__width}, height={self.__height})"
