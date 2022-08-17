#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a square
    """
    def __init__(self, size):
        """Initializes the square
        Args:
            size (int): size of the square
        """
        self.__size = size

    def get_size():
        """getter of __size
        Returns:
            size of the square
        """
        return self.__size

    def set_size(self, size):
        """setter of ___size
        Args:
            value (int): size of the square
        Returns:
            None
        """
        self.__size = size
