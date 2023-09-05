#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Devide two integers """
    new_matrix = matrix[:]
    if isinstance(new_matrix, list):
        for row in new_matrix:
            for num in row:
                if not isinstance(num, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) == len(matrix[1]):
            if isinstance(div, int) or isinstance(div, float):
                if (div == 0):
                    raise ZeroDivisionError("division by zero")
                elif (isinstance(div, str)):
                    raise TypeError("div must be a number")
                else:
                    return [[round(num / div, 2) for num in row] for row in matrix]

            else:
                raise TypeError("div must be a number")
        else:
            raise TypeError("Each row of the matrix must have the same size")

    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
