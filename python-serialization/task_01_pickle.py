#!/usr/bin/python3
"""
Pickling Custom Classes
"""

import pickle


class CustomObject:
    """A custom Python object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file to save the object
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.

        Args:
            filename (str): The file to load the object from

        Returns:
            CustomObject: The deserialized object, or None if error
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError):
            return None
