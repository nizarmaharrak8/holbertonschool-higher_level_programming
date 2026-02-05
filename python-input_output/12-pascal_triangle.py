#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)
        triangle.append(row)

    return triangle
