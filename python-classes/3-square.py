#!/usr/bin/python3
"""Define a class Square with private size and area method."""


class Square:
    """Represent a square with a size attribute and area calculation."""

    def __init__(self, size=0):
        """Initialize a square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
