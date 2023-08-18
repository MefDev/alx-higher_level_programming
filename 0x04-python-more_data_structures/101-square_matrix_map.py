#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    return list(map(lambda lst: list(map(lambda x: x**2, lst)), new_matrix))
