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
    a_list = []
    if len(argv) == 1:
        save_to_json_file(a_list, filename)
    else:
        a_list = load_from_json_file(filename)
        for i in range(1, len(argv)):
            a_list.append(argv[i])
            save_to_json_file(a_list, filename)
