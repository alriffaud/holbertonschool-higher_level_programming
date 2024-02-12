#!/usr/bin/python3
"""
In this module, the Base class is defined.
Classes:
- Base: This class will be the “base” of all other classes in this project.
"""


class Base:
    """
    This class will be the “base” of all other classes in this project.
    Class Attributes:
    - __nb_objects: This represents the number of objects created.
    Methods:
    - __init__: This is the initialization method.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization method.
        Parameters:
          - id: This is the identification number of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
