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

    @property
    def size(self):
        """
        This method returns the size of the rectangle.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        This method sets the value of size.
        Parameters:
          - value: It's the new size value.
        """
        setattr(self, 'width', value)
        setattr(self, 'height', value)

    def __str__(self):
        """
        This method return a string representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None:
                    super().update(id=args[0])
            if len(args) > 1:
                setattr(self, 'size', args[1])
            if len(args) > 2:
                setattr(self, 'x', args[2])
            if len(args) > 3:
                setattr(self, 'y', args[3])
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().update(id=value)
                elif key in ['size', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Square.
        """
        if self is None:
            return (None)
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
