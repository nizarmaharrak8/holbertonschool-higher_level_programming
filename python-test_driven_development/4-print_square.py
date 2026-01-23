#!/usr/bin/python3
"""Module to print a square with the character '#'.

This module contains the function print_square(), which prints
a square of '#' characters with side length equal to the given size.
It performs strict input validation to ensure
 the size is a non-negative integer.
"""


def print_square(size):
    """Prints a square with the character '#' of given side length.

    The function prints a square where both the width and height are equal
    to the value of 'size'. Each line consists of '#' repeated 'size' times.

    Args:
        size (int): The side length of the square.
          Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer (e.g., float, str, list, etc.).
        ValueError: If size is a negative integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    if size > 0:
        for i in range(size):
            print("#" * size)
