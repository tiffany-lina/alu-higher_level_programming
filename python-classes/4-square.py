#!/usr/bin/python3
"""Define a class Square with private size, getter/setter, and area method."""


class Square:
    """Represent a square with a size attribute and area calculation."""

    def __init__(self, size=0):
        """Initialize a square with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
