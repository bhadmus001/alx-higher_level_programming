#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Represent a square
    Attributes:
        __size(int): size of  square
    """
    def __init__(self, size=0):
        """initializes the object square
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
