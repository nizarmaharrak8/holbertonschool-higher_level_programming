#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

