#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    count = 1
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
        print("1: {0}".format(argv[1]))
    else:
        print("{0}: arguments:".format(arg_len))
        for arg in argv[1:]:
            print("{}: {}".format(count, arg))
            count += 1
