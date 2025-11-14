#!/usr/bin/python3
"""This module defines the BaseGeometry class with area and integer validation methods."""


class BaseGeometry:
    """BaseGeometry class to serve as a base for geometric shapes."""

    def area(self):
        """Calculate the area of a geometric shape.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
