#!/usr/bin/python3

"""
A Square Module
"""


class Square:
    """
    A square class containing a private attribute.

    Args:
        size(int): The size of the square

    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Function that calculates and returns the area of the square"""
        return self.__size ** 2
