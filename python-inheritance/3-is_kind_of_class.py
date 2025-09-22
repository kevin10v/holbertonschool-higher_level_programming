#!/usr/bin/python3
"""
This module defines the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or of a class
    that inherited from a_class.

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        bool: True if obj is an instance or subclass instance of a_class,
        False otherwise
    """
    return isinstance(obj, a_class)
