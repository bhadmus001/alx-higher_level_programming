#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represent a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes the square object
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of the square
        Returns:
            int: if successful
        """
        return self.__size**2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError('size must be integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
