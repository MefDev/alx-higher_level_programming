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
