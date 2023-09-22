#!/usr/bin/python3
"""
This module defines a function to look up attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
        obj (object): The object to inspect.
    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
