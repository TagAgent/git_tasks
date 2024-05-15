class Rectangle:
    def __init__(self, height_pm, width_pm):
        self.width = width_pm
        self.height = height_pm

    def calculate_square(self):
        result = self.height * self.width
        return result

    def calculate_perimetr(self):
        result = self.height * 2 + self.width * 2
        return result

r1 = Rectangle(height_pm=4 ,width_pm=5)
r2 = Rectangle(height_pm=15, width_pm=2)

sqr1 = r1.calculate_square()

pr1 = r1.calculate_perimetr()

print(pr1)

