#!/usr/bin/python3
"""
Function that returns the dictionary description
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    suitable for JSON serialization

    Args:
        obj: instance of a Class

    Returns:
        dict: dictionary containing all serializable attributes
    """
    return obj.__dict__
