#!/usr/bin/python3
"""
Now the object itself, the Square, has evolved it's own conssiunes into a sentient-like state.
For it is only sentient to be aware of one's own might.
"""


class Square:
    """Defines the Square Class"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        size = self.__size
        return (size * size)
