#!/usr/bin/python3

"""
A Square Module
"""


class Square:
    """
    A square class containing a private attribute.

    Args:
        size(int): The size of the square

    Raises:
            TypeError: If value isn't an integer
            ValueError: if value is less than zero
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: Get the size of the Square

        The setter sets the size of the Square

        Args:
            value(int): The new size of the square, value should be >= 0

        Raises:
            TypeError: If value isn't an integer
            ValueError: if value is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that calculates and returns the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
