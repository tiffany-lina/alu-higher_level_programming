#!/usr/bin/python3
"""Defines a Student class with JSON serialization/deserialization"""


class Student:
    """Represents a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
