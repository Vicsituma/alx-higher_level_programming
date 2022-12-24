#!/usr/bin/python3
"""defining a square"""


class Square:
    """a class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization of the square class using size"""
        self.__size = size
        self.__posotion = position

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

    @property
    def position(self):
        """"retrieves position"""
        return self.__position

    @position.setter
    def position(self, pos):
        """sets new position value"""
        if isinstance(pos, tuple) and len(pos) == 2
        and pos[1] >= 0 and pos[2] >= 0:
            self.__position = pos
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates the area of the square"""
        return (self.__size**2)

    def my_print(self):
        """ prints in stdout the square with the character #:
        if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
