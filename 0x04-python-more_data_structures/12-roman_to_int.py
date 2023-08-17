#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for char in roman_string:
        for key, val in dic.items():
            if (char == key):
                if (char == "I" and roman_string[0] == "I"):
                    sum -= val
                else:
                    sum += val
    return sum
