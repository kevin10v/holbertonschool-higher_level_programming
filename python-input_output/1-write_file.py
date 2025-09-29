#!/usr/bin/python3
"""
Module 1-write_file
Function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.
    Creates the file if it doesn’t exist,
    and overwrites it if it does.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
