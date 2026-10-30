# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    height = 0
    width = 0
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if(type(width) != int):
            raise TypeError
        if(type(height) != int):
            raise TypeError

        if (width <= 0):
            raise ValueError
        if (height <= 0):
            raise ValueError
        self.width = width
        self.height = height

    def is_square(self):
        """ returns whether the rectangle is a square"""
        return self.width == self.height
    def area(self):
        """ returns the area of the rectangle"""
        return self.width * self.height
    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        return self.width * 2 + self.height * 2
    
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
