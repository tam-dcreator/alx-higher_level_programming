#!/usr/bin/python3

"""A lookup function module"""


def lookup(obj):
    """A function to get the attributes of an object.

    Args:
        obj(object): The first parameter

    Returns:
        list:A list of attributes available to an object
    """
    return dir(obj)
