#!/usr/bin/python3
import sys
num_of_args = len(sys.argv) - 1
if num_of_args == 0:
    print("0 arguments.")
else:
    if num_of_args == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, num_of_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
