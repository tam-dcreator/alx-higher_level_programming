#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    arg_len = len(argv) - 1
    operator = {'+': add, '-': sub, '*': mul, '/': div}

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    sym = argv[2]
    b = int(argv[3])

    if sym not in operator.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, sym, b, operator[sym](a, b)))
