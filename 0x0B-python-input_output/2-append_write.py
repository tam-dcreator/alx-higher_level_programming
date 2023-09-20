#!/usr/bin/python3
"""
Module containing a function that appends to a file.
"""


def append_write(filename="", text=""):
    """ Function that appends to an existing file, if the file doesn't exist
    it creates the file.

    Args:
        filename(str): Path to the file
        text(str): Content to be written to the file

    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
