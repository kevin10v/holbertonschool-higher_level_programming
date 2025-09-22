#!/usr/bin/python3
"""
This module defines the lookup function
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: object to inspect

    Returns:
        list: attributes and methods of the object
    """
    return dir(obj)
