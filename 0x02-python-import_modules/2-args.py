#!/usr/bin/python3
import sys
num_of_args = len(sys.argv) - 1
if num_of_args == 0:
    print("0 arguments.")
else:
    if num_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, num_of_args + 1):
            print("{}: {} arguments:".format(i, sys.argv[i]))
