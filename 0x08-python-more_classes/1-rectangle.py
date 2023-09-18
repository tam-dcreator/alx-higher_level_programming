#!/usr/bin/python3
"""
A Module for a Rectangle Class
"""


class Rectangle:
    """ A rectangle class with its properties defined

    Args:
        width(int): The width of the rectangle
        height(int): The height of the rectangle

    Raises:
        TypeError: If width or height are not integers
        ValueError: If width or height is less than zero
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """int: Get the width of the Rectangle

        The setter sets the width

        Args:
            value(int): The new width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the Rectangle

        The setter sets the height of the rectangle

        Args:
            value(int): The new height

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
