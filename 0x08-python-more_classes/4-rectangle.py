#!/usr/bin/python3
""" empty class Rectangle that defines arectangle """


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """ instantiation of rectangle with optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ area """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ return the rectangle with character # """
        H = self.__height
        W = self.__width
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#".join([(S) for i in range(W)]) for j in range(H)])

    def __repr__(self):
        """ return  a string rpresentation of this rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
