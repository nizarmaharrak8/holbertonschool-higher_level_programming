#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The function matrix_divided takes a matrix (list of lists) and a divisor,
validates the inputs, divides each element by
the divisor, rounds to 2 decimal places,
and returns a new matrix with the results.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows are not the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not matrix:
        return []
    row_length = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
