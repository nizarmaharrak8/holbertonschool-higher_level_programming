#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """
       Represents a square with a private size attribute.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
    @property
    def size(self):
        """
		Docstring for size
		
		:param self: Description
		"""
        return self.__size

    @size.setter
    def size(self, value):
        """
		Docstring for size
		
		:param self: Description
		:param value: Description
		"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
