#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_constructor(self):
        """Test the constructor of Rectangle"""
        r = Rectangle(10, 5)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_custom_id(self):
        """Test the custom id of rectangle class"""
        r = Rectangle(10, 20, 5, 2, 120)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 120)

    def test_setters(self):
        """Test setter of rectangle class"""
        r = Rectangle(10, 20)
        r.height = 50
        r.width = 100
        r.x = 30
        r.y = 25

        self.assertEqual(r.height, 50)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 25)

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
