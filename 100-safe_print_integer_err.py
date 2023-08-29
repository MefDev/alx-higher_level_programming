#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except ValueError as valErr:
        sys.stderr.write("Exception: {}".format(valErr))
    except TypeError as typeErr:
        sys.stderr.write("Exception: {}".format(typeErr))
