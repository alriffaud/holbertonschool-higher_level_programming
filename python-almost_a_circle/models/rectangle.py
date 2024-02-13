#!/usr/bin/python3
"""
In this module, the Rectangle class is defined.
Classes:
- Rectangle: This class defines a rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class defines a rectangle.
    Attributes:
    - __width: This is the width of the rectangle.
    - __height: This is the height of the rectangle.
    Methods:
    - width(self):  This method returns the width of the rectangle.
    - width(self, value): This method sets the value of width.
    - height(self): This method returns the height of the rectangle.
    - height(self, value): This method sets the value of height.
    - x(self): This method returns the x position of the rectangle.
    - y(self): This method returns the y position of the rectangle.
    - x(self, value): This method sets the value of x.
    - y(self, value): This method sets the value of y.
    - area(self): This method returns the area of the rectangle.
    - display(self): This method prints in stdout the rectangle with the
    character #.
    - __str__: Is responsible for returning a string representation of the
    rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the initialization method.
        Parameters:
          - width: This is the width of the rectangle.
          - height: This is the height of the rectangle.
          - x: This is the x coordinate.
          - y: This is the y coordinate.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        This method returns the width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        This method sets the value of width.
        Parameters:
          - value: It's the new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This method returns the height of the rectangle.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        This method sets the value of height.
        Parameters:
          - value: It's the new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        This method returns the x position of the rectangle.
        """
        return (self.__x)

    @property
    def y(self):
        """
        This method returns the y position of the rectangle.
        """
        return (self.__y)

    @x.setter
    def x(self, value):
        """
        This method sets the value of x.
        Parameters:
          - value: It's the new x value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        This method sets the value of y.
        Parameters:
          - value: It's the new y value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns the area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        This method prints in stdout the rectangle with the character #.
        """
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        This method return a string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None:
                    self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value
