#!/usr/bin/python3
"""
Module containing function that returns a dictionary representation of a class
"""


def class_to_json(obj):
    """Function that returns the dictionary representation of a class

    Args:
        obj(obj): Instance of a class

    Returns:
        dict: Dictionary representation of the class
    """
    return obj.__dict__
