#!/usr/bin/python3
"""
Function that returns the dictionary description of a class instance
with simple data structures (list, dict, string, int, bool)
suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary containing all serializable attributes of `obj`.
    """
    return obj.__dict__.copy()
