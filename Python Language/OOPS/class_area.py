from math import pi

class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius**2

class rec():
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
c = circle(int(input("Enter the radius: ")))
r = rec(int(input("Enter the length: ")), int(input("Enter the width: ")))


print(f"Area of circle: {c.area():.2f}")
print(f"Area of rectnagle: {r.area()}")