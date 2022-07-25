#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if int(value) and value >= 0:
                self.__width = value
        except TypeError:
            print("width must be integer")
        except ValueError:
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if int(value) and value >= 0:
                self.__height = value
        except TypeError:
            print("height must be integer")
        except ValueError:
            print("height must be >= 0")
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
