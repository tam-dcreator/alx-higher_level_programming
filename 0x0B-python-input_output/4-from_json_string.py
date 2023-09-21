#!/usr/bin/python3
"""
Module containing a function that converts a json string to python data obj
"""


def from_json_string(my_str):
    """Function that returns a python data structure from a json string

    Args:
        my_str(str): Json string
    Returns:
        obj: Python data structure
    """
    import json
    return json.loads(my_str)
