#!/usr/bin/python3
"""
A Module for a MagicClass
"""
from math import pi


class MagicClass:
    """
    A Magic class, that replicates a disassembled bytecode commands

    Args:
        radius(int/float): Number representing the radius of the object
    """
    def __init__(self, radius=None):
        if radius is not int or radius is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Function to find the area when the radius is provided"""
        return pi * (self.__radius ** 2)

    def circumference(self):
        """Function to find the circumference given the radius"""
        return 2 * pi * self.__radius
