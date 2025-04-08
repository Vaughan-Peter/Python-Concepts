from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
circle2 = Circle(9)
rectangle2 = Rectangle(7, 9)

print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Circle 2:", circle2.area())
print("Area of Rectangle 2:", rectangle2.area())