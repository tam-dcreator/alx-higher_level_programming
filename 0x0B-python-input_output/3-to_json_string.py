#!/usr/bin/python3
"""
Module that contains a function that returns a Json representation of an object
"""


def to_json_string(my_obj):
    """ Function that returns the json representation of an object

    Args:
        my_obj: The Object to be serialized

    Returns:
        str: Json representation of my_obj
    """
    import json
    return json.dumps(my_obj)
