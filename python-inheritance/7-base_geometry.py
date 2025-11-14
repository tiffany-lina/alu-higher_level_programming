#!/usr/bin/python3
"""Module 7-base_geometry: Defines BaseGeometry class with validation."""

class BaseGeometry:
    """BaseGeometry class that defines geometric operations."""

    def area(self):
        """Calculate area.

        Raises:
            Exception: Always raises 'area() is not implemented'
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

