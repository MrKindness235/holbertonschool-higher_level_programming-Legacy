#!/usr/bin/python3
"""
This is the third installment of the Square Class. 
Now it is more complex, and has more "Concioussness".
Thank you Luz for helping with this!
"""


class Square:
    """Defines the Square class"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
