#!/usr/bin/python3
for i in range(0, 99):
    if (i <= 9):
        print("0", end="")
    print("{:d}".format(i, i), end=", ")
print(99)
