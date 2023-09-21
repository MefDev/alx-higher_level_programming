#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

        self.assertEqual(b1.id, 6)
        self.assertEqual(b2.id, 120)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 8)
        self.assertEqual(b5.id, 16)

    def test_json_custom_values(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary, {'id': 5, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(
            json_dictionary, '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertEqual(type(json_dictionary), str)

    def test_json_empty_none_values(self):
        EMPTY = []
        NONE_VALUE = None
        empty_json_dictionary = Base.to_json_string(EMPTY)
        self.assertEqual(empty_json_dictionary, "[]")
        self.assertEqual(type(empty_json_dictionary), str)

        none_value_json_dict = Base.to_json_string(NONE_VALUE)
        self.assertEqual(none_value_json_dict, "[]")
        self.assertEqual(type(none_value_json_dict), str)

    def test_save_to_file_custom_values(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        self.assertEqual(Rectangle.save_to_file(
            [r1, r2]), '[{"id": 8, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_save_to_file_None_values(self):
        r1 = None
        self.assertEqual(Rectangle.save_to_file(r1), '[]')

    
    def test_from_json_string_custom_values(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)