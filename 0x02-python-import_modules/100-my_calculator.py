#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1.py import *
    args = sys.argv[1:]
    a = int(args[0])
    b = int(args[2])
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if arg1[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if args[1] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[1] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[1] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[1] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
