#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num = len(args)
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument:".format(num))
        print("{:d}: {}".format(num, args[num]))
    else:
        print("{:d} arguments:".format(num))
        for n in range(1, num + 1):
            print("{:d}: {}".format(n, args[n-1]))
