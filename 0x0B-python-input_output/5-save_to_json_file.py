#!/usr/bin/python3
"""
Module with a function that saves a json representation of an object in a file
"""


def save_to_json_file(my_obj, filename):
    """Function that converts a python object to a json string and saves it in
    a file.

    Args:
        my_obj(): Python data to be saved
        filename(): Path to file where it would be stored

    """
    import json

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
