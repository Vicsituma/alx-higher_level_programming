#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(mylist[i], end="")
    except:
        print("can't print")
    return i
