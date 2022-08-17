#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represent a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square object
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is less than 0
        Returns:
            None
        """
        self.__size = size
        self.position = position

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

    def my_print(self):
        """Prints the square
        Returns:
            None
        """
        if self.size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        '''if self.__position[1] > 0:
        print()'''
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.size):
                print("#", end='')
            print()

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of __position
        Args:
            value (tuple): position of the aquare in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
