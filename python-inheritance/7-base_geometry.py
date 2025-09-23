#!/usr/bin/python3
"""
7-base_geometry.py
Defines a class BaseGeometry with area() and integer_validator().
"""


class BaseGeometry:
    """Class with methods area and integer_validator."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer > 0.

        Args:
            name (str): Name of the variable.
            value (int): Value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
