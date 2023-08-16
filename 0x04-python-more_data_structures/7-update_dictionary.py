#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dictionary = a_dictionary.copy()
    if key in new_dictionary:
        a_dictionary[key] = value
    if key not in new_dictionary:
        a_dictionary[key] = value
    return new_dictionary
