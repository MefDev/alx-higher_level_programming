#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned
last_digit_val = last_digit(number)
stringVal = "Last digit of"
greatThanFive = "and is greater than 5"
lessThanSix = "and is less than 6 and not 0"
isZero = "and is 0"
if (last_digit_val > 5):
    print(f"{stringVal} {number} is {last_digit_val} and {greatThanFive}")
elif last_digit_val == 0:
     print(f"{stringVal} {number} is {last_digit_val} and {isZero}")
else:
    print(f"{stringVal} {number} is {last_digit_val} and {lessThanSix}")
