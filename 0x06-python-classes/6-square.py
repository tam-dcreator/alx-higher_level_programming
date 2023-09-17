#!/usr/bin/python3

"""
A Square Module
"""


class Square:
    """
    A square class containing a private attribute.

    Args:
        size(int): The size of the square
        position(tuple): The position

    Raises:
            TypeError: If value isn't an integer
            ValueError: if value is less than zero
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for elem in position:
            if not isinstance(elem, int) or elem < 0 or len(position) != 2:
                raise TypeError
            ("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """:obj:tuple of :obj:int: Get the position

        The setter sets the new position

        Args:
            value(tuple): The new  position, values should be integers >= 0

        Raises:
            TypeError: If value isn't an integer or value is less than zero
        """
        return self.__position

    @position.setter
    def position(self, value):
        for elem in value:
            if not isinstance(elem, int) or elem < 0 or len(value) != 2:
                raise TypeError
            ("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function that calculates and returns the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Function that prints the square using the pound sign"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                if not self.__position[1] > 0:
                    for _ in range(self.__position[0]):
                        print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
