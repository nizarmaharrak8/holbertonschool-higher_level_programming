#!/usr/bin/python3
"""
Returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string"""
    return json.dumps(my_obj)
