#!/usr/bin/python3
"""
This module defines the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        bool: True if obj is instance of a subclass of a_class,
        False if obj is instance of a_class itself or unrelated class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
