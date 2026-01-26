#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """
        Docstring for position
        
        :param self: Description
        """
        return self.__size
    @position.setter
    def position(self, value):
        """
        Docstring for position
        
        :param self: Description
        :param value: Description
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__size = value

    def my_print(self):
        """Prints the square with the character"""
        if self.__size == 0:
            print()
        if self.__size >= 1:
            for i in range(self.__size):
                print("#" * self.__size)
