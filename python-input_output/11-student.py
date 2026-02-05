#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and deserialization.
"""


class Student:
    """Represents a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes in this list
        are included.
        """
        if isinstance(attrs, list):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from the given dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
