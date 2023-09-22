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

    def to_json(self, attrs=None):
        """Function that returns the dictionary representation of this class

        Args:
            atrs(list): List of strings
        Returns:
            dict: Dictionary representation of a class instance
        """
        if isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items() if
                    key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Function that loads class attributes from a file

        Args:
            json(dict): File containing a dictionary for the attributes
        """
        try:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        except Exception:
            return
