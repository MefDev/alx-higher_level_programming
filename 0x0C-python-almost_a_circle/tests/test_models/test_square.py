#!/usr/bin/python3
import unittest
# Import the Rectangle class from the appropriate location
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_valid_attributes(self):
        # Test valid attributes with no exceptions raised
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_invalid_width(self):
        # Test invalid width (not an integer)
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3)

        # Test width <= 0
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 2, 3)

    def test_invalid_height(self):
        # Test invalid height (not an integer)
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 2, 3)

        # Test height <= 0
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 2, 3)

    def test_invalid_x(self):
        # Test invalid x (not an integer)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3)

        # Test x < 0
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_invalid_y(self):
        # Test invalid y (not an integer)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid")

        # Test y < 0
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3)

    def test_set_attributes(self):
        # Test setting valid attributes using setters
        rect = Rectangle(5, 10, 2, 3)
        rect.width = 8
        self.assertEqual(rect.width, 8)

        rect.height = 15
        self.assertEqual(rect.height, 15)

        rect.x = 4
        self.assertEqual(rect.x, 4)

        rect.y = 6
        self.assertEqual(rect.y, 6)

    def test_set_invalid_attributes(self):
        # Test setting invalid attributes using setters
        rect = Rectangle(5, 10, 2, 3)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = 0

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = 0

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -2

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -3
