#!/usr/bin/python3
"""add_integer function."""


def add_integer(a, b=98):
    """Return sum of a and b as ints."""
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
