#!/usr/bin/python3
"""
Module with a function that loads a json file and returns a python object
"""


def load_from_json_file(filename):
    """Function that loads a json string from a file, converts it to a python
    object and returns it

    Args:
        filename(str): Path to the file containing the string

    Returns:
        obj: A python data object
    """
    import json
    with open(filename, "r") as file:
        return json.load(file)
