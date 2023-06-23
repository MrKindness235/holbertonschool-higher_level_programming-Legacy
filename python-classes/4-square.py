#!/usr/bin/python
"""
Now, the object can be modified by the world of data sorrounding it
garnting it a philosphical sense of flow, which is to say,
pull, push and touch.
"""


class Square:
    """This, is a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)
    """This is a method that calls forth the Square's main property, it's size."""

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an interger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value
    """A setter, made to recall the data property and to be affixed to the square"""

    def area(self):
        size = self.__size
        return (size * size)
    """
    With this las method, one can make the Square calculate itself,
    giving it a sense of concioussness
    """
