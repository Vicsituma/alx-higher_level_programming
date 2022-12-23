#!/usr/bin/python3
"""defining a square"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0):
        """initialization of the square class using size"""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculates the area of the square"""
        return (self.__size**2)
