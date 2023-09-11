#!/usr/bin/python3

"""Module of a function is_same_class """


def is_same_class(obj, a_class):
    """Function that checks if an object is exacly an instance of a specified
    class.

    Args:
        obj(Object): An object to cross check
        a_class(Class): Corresponding class to check against

    Returns:
    bool: True if it is exact, False if it isnt.
    """
    if type(obj) == a_class:
        return True
    return False
