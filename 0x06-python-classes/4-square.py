#!/usr/bin/python3
    """Defines a square."""
class Square:
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of square.

        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.


        Args:
            size: Length of a side of square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):

        return self.__size ** 2
