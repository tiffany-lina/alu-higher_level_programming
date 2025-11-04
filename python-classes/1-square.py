#!/usr/bin/python3
"""This module defines a class Square with a private instance attribute size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

