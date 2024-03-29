#!/usr/bin/python3
"""
In this module, a 'Student' class is defined.
"""


class Student:
    """
    This class defines a student.
    Attributes:
    - first_name: This is the student first name.
    - last_name: This is the student last name.
    - age: This is the student age.
    Methods:
    - to_json: Retrieves a dictionary representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        This is the initialization method.
        Parameters:
        - first_name: This is the student first name.
        - last_name: This is the student last name.
        - age: This is the student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method retrieves a dictionary representation of a Student
        instance.
        """
        json_dict = {}
        attributes = self.__dict__
        for key, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
        return (json_dict)
