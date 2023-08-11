#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_of_args = len(sys.argv) - 1
    if num_of_args == 0:
        print(f"{num_of_args}")
    else:
        sum = 0
        for i in range(1, num_of_args + 1):
            sum += int(sys.argv[i])
        print(f"{sum}")
