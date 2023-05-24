# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width 
    
    def perimeter(self):
        return self.length*2 + self.width*2

    def __str__(self) -> str:
        return f'area of rectangle is: {self.area()}\nperimeter is: {self.perimeter()}'

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        
    def area(self):
        return self.radius**2 * 3.14

    def circum(self):
        return 2*3.14*self.radius

    def __str__(self) -> str:
        return f'area of circle is: {self.area()}\ncircumference is: {self.circum()}'
    
circ = Circle(3)
rect = Rectangle(4,10)

print(circ)
print(rect)