from math import sqrt
class Triangle:
    def __init__(self, first_side_pm: int, second_side_pm: int, third_side_pm: int):
        self.first_side = first_side_pm
        self.second_side = second_side_pm
        self.third_side = third_side_pm

    def calculate_perimetr(self) -> int:
       """Этот метод для вычисления периметра треугольника"""
       perimetr = self.first_side + self.second_side + self.third_side
       return perimetr

    def calculate_square(self):
        """Этот метод для вычисления площади треугольника"""
        p = self.calculate_perimetr()/2
        square = sqrt(p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side))
        return square

triamgle1 = Triangle(first_side_pm=2, second_side_pm=2, third_side_pm=2)
triamgle2 = Triangle(first_side_pm=4, second_side_pm=5, third_side_pm=3)

print(triamgle1.calculate_perimetr())
print(triamgle1.calculate_square())
print()
print(triamgle2.calculate_perimetr())
print(triamgle2.calculate_square())
