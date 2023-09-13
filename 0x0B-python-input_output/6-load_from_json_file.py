#!/usr/bin/python3
"""function creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Load from json file"""
    with open(filename, encoding="UTF-8") as a_file:
        return json.loads(a_file.read())
