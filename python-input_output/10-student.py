#!/usr/bin/python3
"""
Defines a class Student with JSON serialization and filtering
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance

        Args:
            attrs (list, optional): list of attribute names to retrieve.
                                    If None or not a list of strings,
                                    all attributes are retrieved.

        Returns:
            dict: dictionary with requested attributes
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
