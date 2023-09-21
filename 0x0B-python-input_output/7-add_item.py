#!/usr/bin/python3
"""
A script that adds all arguments to a python list and then saves them in a file
"""


from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "6-load_from_json_file").load_from_json_file

    filename = "add_item.json"
    try:
        a_list = load_from_json_file(filename)
    except FileNotFoundError:
        a_list = []
    a_list.extend(argv[1:])
    save_to_json_file(a_list, filename)
