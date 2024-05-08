import functional

print("Это программа для вычисления результата арифметических операции с целыми числами")
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
operation_char = input("Введите операцию (+, -, /, *):")
functional.arifmetic_calculations(num1, num2, operation_char)