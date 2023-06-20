#!/usr/bin/python
class Square:
    def size(self):
        return (self.value)

    def size(self, value):
        self.value = value

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        size = self.__size
        return (size * size)
