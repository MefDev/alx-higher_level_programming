#!/usr/bin/python3
"""
a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Pascal tri"""
    pascal_tri_list = []
    prevN = []
    for i in range(n):
        atN = [1] + [sum(prevN[ele:ele + 2]) for ele in range(len(prevN) - 1)]
        if i > 0:
            atN = atN + [1]
        pascal_tri_list.append(atN)
        prevN = atN
    return pascal_tri_list
