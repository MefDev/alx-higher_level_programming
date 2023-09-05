#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test for max_integer """

    def test_positive(self):
        """ test positive values """
        self.assertEqual(max_integer([2, 2, 4]), 4)
    def test_negative(self):
        """ test negative values """
        self.assertEqual(max_integer([-2, -3, -4]), -2)
    def test_empty(self):
        """ test empty list """
        self.assertEqual(max_integer([]), None)
    def test_strings(self):
            """ test strings values """
            self.assertEqual(max_integer(["A", "B", "C", "D"]), "D")
    def test_one_value(self):
          """ test one value """
          self.assertEqual(max_integer([2]), 2)
    def test_mix_values(self):
        """ test one value """
        self.assertEqual(max_integer([2, -2, 40]), 40)

    