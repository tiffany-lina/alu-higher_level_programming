#!/usr/bin/python3
"""BaseGeometry class with area and integer validation."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
