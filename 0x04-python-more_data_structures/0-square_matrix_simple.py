#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_squared = []
    for list_of_nums in new_matrix:
        list_of_nums = list(map(lambda x: x**2, list_of_nums))
        new_squared.append(list_of_nums)
    return new_squared
