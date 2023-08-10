#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    length = len(str)
    for i in range(length):
        if i == n:
            continue
        new_str += str[i]
    return new_str
