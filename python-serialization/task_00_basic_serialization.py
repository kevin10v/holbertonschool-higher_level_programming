#!/usr/bin/python3
"""
Basic serialization and deserialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file

    Args:
        data (dict): Python dictionary
        filename (str): name of the file to save JSON into
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it back to a Python dictionary

    Args:
        filename (str): name of the file containing JSON

    Returns:
        dict: Python dictionary with deserialized data
    """
    with open(filename, 'r') as f:
        return json.load(f)
