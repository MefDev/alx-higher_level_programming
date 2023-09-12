#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8) and
returns the number of characters writte"""


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        return a_file.write(text)
