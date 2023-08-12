#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    num_of_args = len(sys.argv) - 1
    if num_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

    a = sys.argv[1]
    oper = sys.argv[2]
    b = sys.argv[3]
    if oper == "+":
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        exit(0)
    elif oper == "*":
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        exit(0)
    elif oper == "-":
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        exit(0)
    elif oper == "/":
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
