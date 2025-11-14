#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list."""


class MyList(list):
    """A list subclass with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original."""
        print(sorted(self))
