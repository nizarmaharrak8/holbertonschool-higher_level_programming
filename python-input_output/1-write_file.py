#!/usr/bin/python3
"""
Writes a string to a text file (UTF-8).
Returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
