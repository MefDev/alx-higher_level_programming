#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for number in list:
            if (number % 3 != 0):
                print("{:d}".format(number), end=" ")
            else:
                print("{:d}".format(number), end="")
        print()
