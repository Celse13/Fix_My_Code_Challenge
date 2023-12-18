#!/usr/bin/python3
"""The class of the square"""


class Square:
    """Implementation of the square."""
    width = 0
    height = 0

    def __init__(self, **kwargs):
        """Instationa of my square."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Perimeter of my square"""
        return (self.width + self.height) * 2

    def __str__(self):
        """Representaion of my square in string form."""
        return f"{self.width}/{self.height}"


if __name__ == "__main__":
    """Main module"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
