#!/usr/bin/python3
"""
Module that contains a function to write text to a file
"""


def write_file(filename="", text=""):
    """Function to write a string to a file

    Args:
        filename(str): The path to the file
        text(str): Text content to be written

    Returns:
        int: The number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
