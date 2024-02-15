#!/usr/bin/python3
"""
In this module, the Base class is defined.
Classes:
- Base: This class will be the “base” of all other classes in this project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string representation of
        list_dictionaries.
        Parameters:
        - list_dictionaries: is a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of list_objs to a
        file.
        Parameters:
        - cls: is the class itself.
        - list_objs: is a list of instances who inherits of Base.
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string representation.
        Parameters:
        - json_string:  is a string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance with all attributes already set.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            instance = Rectangle(2, 3)
        elif cls.__name__ == "Square":
            instance = Square(2)
        else:
            raise ValueError("Unsupported class")
        instance.update(**dictionary)
        return (instance)
