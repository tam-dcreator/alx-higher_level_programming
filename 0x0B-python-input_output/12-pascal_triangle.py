#!/usr/bin/python3
"""
A module for a pascals triangle generator function
"""


def pascal_triangle(n):
    """ A function that generates a pascals triangle representation in a list

    Args:
        n(int): Pascal triangle length
    Returns:
        list: Nested list containing the pascals triangle at every value
              starting from 1 to n

    """
    if type(n) is not int:
        return
    triangle = []

    for i in range(n):
        tri_line = []

        for j in range(i + 1):
            if j == 0 or j == i:
                tri_line.append(1)
            elif j > 0 and i > 0:
                next_line = triangle[i - 1][j - 1] + triangle[i - 1][j]
                tri_line.append(next_line)
        triangle.append(tri_line)
    return triangle
