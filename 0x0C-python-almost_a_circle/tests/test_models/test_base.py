#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_instance_id_auto_increment(self):
        """Test the auto increment of Base"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_custom_value(self):
        """Test the custom value of Base"""
        b1 = Base(15)
        b2 = Base(150)

        self.assertEqual(b1.id, 15)
        self.assertEqual(b2.id, 150)

    def test_mixed_values(self):
        """Test both custom value and auto increment of Base"""
        b1 = Base()
        b2 = Base(120)
        b3 = Base()
        b4 = Base(8)
        b5 = Base(16)

        self.assertEqual(b1.id, 5)
        self.assertEqual(b2.id, 120)
        self.assertEqual(b3.id, 6)
        self.assertEqual(b4.id, 8)
        self.assertEqual(b5.id, 16)
