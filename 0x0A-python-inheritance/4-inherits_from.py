#!/usr/bin/python3

"""Module of a function inherits_from() """


def inherits_from(obj, a_class):
    """Function that checks if an object is instance of a class that inherited
    from a specified class.

    Args:
        obj(Object): An object to cross check
        a_class(Class): Corresponding class to check against

    Returns:
    bool: True if it is an instance, False if it isnt.
    """
    if a_class.__subclasses__():
        if isinstance(obj, a_class):
            return True
