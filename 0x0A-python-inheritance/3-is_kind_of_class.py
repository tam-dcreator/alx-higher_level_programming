#!/usr/bin/python3

"""Module of a function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is an instance of a class or a class
    that inherited from the specified class.

    Args:
        obj(Object): An object to cross check
        a_class(Class): Corresponding class to check against

    Returns:
    bool: True if it is an instance, False if it isnt.
    """
    return isinstance(obj, a_class)
