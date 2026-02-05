#!/usr/bin/python3
"""
Returns the dictionary description of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """Returns a dictionary with all serializable attributes of obj"""
    return obj.__dict__

