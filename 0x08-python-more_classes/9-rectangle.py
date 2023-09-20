#!/usr/bin/python3
"""
A Module for a Rectangle Class
"""


class Rectangle:
    """ A rectangle class with its properties defined

    Args:
        width(int): The width of the rectangle
        height(int): The height of the rectangle
        number_of_instances(int): Gives the number of instances of this class
        print_symbol(any type): Used as a symbol for string representation

    Raises:
        TypeError: If width or height are not integers
        ValueError: If width or height is less than zero
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1
        self.print_symbol = type(self).print_symbol

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
        self.__height = value

    def area(self):
        """ Finds the area of the rectangle

        Returns:
            int: The calculated area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Finds the perimeter of the rectangle

        Returns:
            int: The calculated perimeter or zero if height/width is zero
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Function to implement a default response when print is called on
        an instance of this class

        Returns:
            str: String representation of the rectangle using #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        self.__return = ""
        for i in range(self.__height):
            self.__return += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                self.__return += "\n"
        return self.__return

    def __repr__(self):
        """Returns a string representation of the Rectangle instance

        This method is called by the built-in 'repr()' function and provides
        a concise representation of the object. Typically used for debugging
        and development purposes

        Returns:
        str: A string representation of the object
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """ The del method for rectangle class
        Performs clean up action before an instance is destroyed.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Function to check the bigger rectangle of two rectangle objects

        Args:
            rect_1: The first Rectangle object
        Args:
            rect_2: The second Rectangle object
        Returns:
             Rectangle object: The bigger rectangle or rect_1 if they are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Function that creates a square using the rectangle class

        Args:
            size(int): The width and height of the rectangle to be created
        Returns:
             Rectangle object: A new rectangle of equal width and height
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        return Rectangle(size, size)
