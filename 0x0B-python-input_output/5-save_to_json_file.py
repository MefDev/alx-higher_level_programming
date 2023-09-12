#!/usr/bin/python3
import json
"""function that writes an Object to a text file,
using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        a_file.write(json.dumps(my_obj))
