#!/usr/bin/python3
"""
Pickling and unpickling a custom class
"""

import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): True if the person is a student, False otherwise
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file

        Args:
            filename (str): The file to save the object to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file

        Args:
            filename (str): The file to load the object from

        Returns:
            CustomObject: The deserialized object, or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
