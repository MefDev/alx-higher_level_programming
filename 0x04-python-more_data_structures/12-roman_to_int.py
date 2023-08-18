#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    if not roman_string:
        return 0
    prev_value = 0
    for char in reversed(roman_string):
        value = dic.get(char)
        if value is None:
            return 0
        if value < prev_value:
            sum -= value
        else:
            sum += value
        prev_value = value
    return sum
