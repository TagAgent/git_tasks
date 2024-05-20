import math
class Circle:
    def __init__(self, radius_pm):
        self.radius = radius_pm

    def calculate_square(self):
        result = (self.radius * self.radius) * math.pi
        return result

circle1 = Circle(radius_pm=10)

sqr1 = circle1.calculate_square()

print(sqr1)
