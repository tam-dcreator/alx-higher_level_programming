#!/usr/bin/python3
"""
Module containing a Student class
"""


class Student:
    """A student class

    Args:
        first_name(str): Student first name
        last_name(str): Student last name
        age(int): Student age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that returns the dictionary representation of this class

        Returns:
            dict: Dictionary representation of a class instance
        """
        return self.__dict__
