#!/usr/bin/python3
"""Demonstrates the usage of the add_integer function."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Default is 98.

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.

    Example:
        result = add_integer(3, 5)  # result will be 8
        result = add_integer(-1, 2)  # result will be 1

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
