#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area and integer_validator."""


class BaseGeometry:
    """BaseGeometry class with validation methods."""

    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer > 0.

        Args:
            name (str): Name of the parameter.
            value: Value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
