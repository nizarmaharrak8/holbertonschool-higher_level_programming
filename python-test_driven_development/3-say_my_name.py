#!/usr/bin/python3
"""Module to print a person's full name.

This module contains the function say_my_name(), which prints
a formatted message with the user's first and last name after
validating that both are strings.

The function enforces strict type checking and raises TypeError
with specific messages if inputs are not of type str.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>".
    Args:
        first_name (str): The first name. Must be a string.
        last_name (str, optional):
                The last name. Defaults to an empty string.
                                   Must be a string if provided.
    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
