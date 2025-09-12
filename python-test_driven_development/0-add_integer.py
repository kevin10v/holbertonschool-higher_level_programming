#!/usr/bin/python3
"""Simple addition module.

Defines add_integer(a, b=98).

Adds two integers with type checks.
"""


def add_integer(a, b=98):
    """Add two integers.

    Floats are cast to ints.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Refuzo NaN dhe ±inf pa importe
    if isinstance(a, float) and (
            a != a or a in (float('inf'), float('-inf'))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (
            b != b or b in (float('inf'), float('-inf'))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
