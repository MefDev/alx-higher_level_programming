#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
