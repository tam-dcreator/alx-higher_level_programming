#!/usr/bin/python3
"""
Module containing function to read and print contents from a file
"""


def read_file(filename=""):
    """Function that reads content from a file

    Args:
        filename(str): Path to the file to be read
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
