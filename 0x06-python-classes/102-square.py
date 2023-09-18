#!/usr/bin/python3

"""
A Square Module
"""


class Square:
    """
    A square class containing a private attribute.

    Args:
        size(int/float): The size of the square

    Raises:
            TypeError: If value isn't a number
            ValueError: if value is less than zero
    """
    def __init__(self, size=0):
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: Get the size of the Square

        The setter sets the size of the Square

        Args:
            value(int/float): The new size of the square, value should be >= 0

        Raises:
            TypeError: If value isn't a number
            ValueError: if value is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that calculates and returns the area of the square

        Returns:
            int/float : The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Function that checks if two square objects are equal

        Returns:
           bool: True or False
        """
        return self.__size == other.size

    def __ne__(self, other):
        """Function that checks if two square objects are not equal

        Returns:
           bool: True or false
        """
        return self.__size != other.size

    def __gt__(self, other):
        """Function that checks if square A is greater than square B

        Returns:
           bool: True or false
        """
        return self.__size > other.size

    def __ge__(self, other):
        """Function that checks if square A is greater or equal to square B

        Returns:
           bool: True or false
        """
        return self.__size >= other.size

    def __lt__(self, other):
        """Function that checks if square A is less than square B

        Returns:
           bool: True or false
        """
        return self.__size < other.size

    def __le__(self, other):
        """Function that checks if square A is less than or equal to square B

        Returns:
           bool: True or false
        """
        return self.__size <= other.size
