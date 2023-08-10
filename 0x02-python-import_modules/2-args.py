#!/usr/bin/python3
import sys
num_of_args = len(sys.argv) - 1
if num_of_args == 0:
    print(f"{num_of_args} arguments.")
else:
    print(f"{num_of_args} arguments:")
    for i in range(1, num_of_args + 1):
        print(f"{i}: {sys.argv[i]}")
