#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """Sort a list"""

    def print_sorted(self):
        print(sorted(self))
