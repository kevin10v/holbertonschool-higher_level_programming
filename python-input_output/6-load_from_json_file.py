#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file to read.

    Returns:
        The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
