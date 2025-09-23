#!/usr/bin/python3
"""
6-base_geometry.py
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """Class with public instance method area."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")
