#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read from a file then print"""
    with open(filename, encoding="UTF-8") as a_file:
        for line in a_file:
            print("{}".format(line), end="")
