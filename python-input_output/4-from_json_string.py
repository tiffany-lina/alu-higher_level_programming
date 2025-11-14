#!/usr/bin/python3
"""
Function that returns the Python object represented
by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by
    the JSON string `my_str`.
    """
    return json.loads(my_str)
