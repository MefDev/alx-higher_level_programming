#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:"""


def append_write(filename="", text=""):
    """Write to a file"""
    with open(filename, mode="a", encoding="UTF-8") as a_file:
        return a_file.write(text)
