import math

class Shape:
    def area(self):
        raise NotImplementedError
        
class Rectangle(Shape):
    def __init__(self, length, width):  # Fixed parameter name
        self.length = length  # Fixed: 'length' not 'lengh'
        self.width = width

    def area(self):
        return self.length * self.width  # Fixed: 'length' not 'lengh'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2