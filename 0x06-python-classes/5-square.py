#!/usr/bin/python3
"""defining a square"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0):
        """initialization of the square class using size"""
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, val):
        """sets new size values"""
        if isinstance(val, int):
            if val >= 0:
                self.__size = val
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculates the area of the square"""
        return (self.__size**2)

    def my_print(self):
        """ prints in stdout the square with the character #:
        if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end='')
