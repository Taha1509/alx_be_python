import math


class Shape:
    def area(self):
        raise NotImplementedError
        
class Rectangle(Shape):
    def __init__ (self, lengh, width):
        self.lengh = lengh
        self.width = width

    def area(self):
        return self.lengh * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2