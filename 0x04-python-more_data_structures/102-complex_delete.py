#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.copy().items():
        if (v is value):
            if (k in a_dictionary):
                del a_dictionary[k]
    return a_dictionary
