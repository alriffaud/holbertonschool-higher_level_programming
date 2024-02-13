#!/usr/bin/python3
"""
In this module, the Rectangle class is defined.
Classes:
- Rectangle: This class defines a rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a square.
    Attributes:
    - __size: This is the size of the square.
    Methods:
    - __str__: Is responsible for returning a string representation of the
    square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the initialization method.
        Parameters:
          - size: This is the size of the square.
          - x: This is the x coordinate.
          - y: This is the y coordinate.
          - id: This is the id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method return a string representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
