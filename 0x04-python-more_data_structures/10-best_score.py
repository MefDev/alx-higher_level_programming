#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if (not a_dictionary):
        return None
    for key in a_dictionary:
        if max < a_dictionary[key]:
            max = a_dictionary[key]
    for key, value in a_dictionary.items():
        if (value == max):
            return key
