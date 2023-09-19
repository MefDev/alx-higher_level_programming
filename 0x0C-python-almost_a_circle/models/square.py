#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the square"""
        if args:
            attribute_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attribute_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        dictionary = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return dictionary

    def __str__(self):
        """String representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
