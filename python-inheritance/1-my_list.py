#!/usr/bin/python3
"""
Module that defines a MyList class inheriting from list
with an additional method to print the list sorted.
"""


class MyList(list):
    """MyList inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
