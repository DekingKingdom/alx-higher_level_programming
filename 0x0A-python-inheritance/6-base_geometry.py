#!/usr/bin/python3

"""Defining an empty  class"""


class BaseGeometry():
    """
    An empty class
    """
    pass

    def area(self):
        """
        Public instance method that calculates the area

        Raises:
            Exception if area is not imlemented
        """
        raise Exception("area() is not implemented")
