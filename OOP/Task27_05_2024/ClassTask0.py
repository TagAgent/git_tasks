import math

def calculate_numbers_multiplication(*numbers):
    result = 1
    for item in numbers:
        result *= item
    return result

print(calculate_numbers_multiplication(1, 12, 15))
print(calculate_numbers_multiplication(2, 2))
