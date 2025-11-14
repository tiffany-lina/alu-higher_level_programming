#!/usr/bin/python3
"""
Function that appends a string to a UTF-8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends `text` to `filename` (UTF-8) and returns
    the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
