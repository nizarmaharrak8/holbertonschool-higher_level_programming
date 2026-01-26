#!/usr/bin/python3
"""docstring for python-classes.0-square"""

class Square:
    """Docstring for Square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

