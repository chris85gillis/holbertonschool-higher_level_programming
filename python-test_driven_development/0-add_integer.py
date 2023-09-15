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

    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))       # Output: 3
    print(add_integer(100, -2))    # Output: 98
    print(add_integer(2))          # Output: 100 (default value of b is 98)
    print(add_integer(100.3, -2))  # Output: 98
    try:
        print(add_integer(4, "School"))  # Raises a TypeError
    except Exception as e:
        print(e)  # Output: "a must be an integer or b must be an integer"

    try:
        print(add_integer(None))  # Raises a TypeError
    except Exception as e:
        print(e)  # Output: "a must be an integer or b must be an integer"
./