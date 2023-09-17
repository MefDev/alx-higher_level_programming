#!/usr/bin/python3

class Base:
    """manage id attribute in all your future classes
    and to avoid duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the code"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
