#!/usr/bin/python3
"""
Writes a Python object to a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a JSON file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
