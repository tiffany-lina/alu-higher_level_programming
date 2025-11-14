#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with private width and height.

        Both width and height are validated as positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return informal string representation of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
