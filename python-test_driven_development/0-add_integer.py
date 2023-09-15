#!/usr/bin/python3
"""Demonstrates the usage of the add_integer function."""


add_integer= __import__('0-add_integer').add_integer
"""Addes two integers and returns their sum.
    Args:
        a (int): The first integer to be added.
        b (int): The second integer to be added.
"""

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
