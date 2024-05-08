
def arifmetic_calculations(num1: int, num2: int, operation_char: str):
    """Calculate result of arifmetic operation"""
    result = 0
    if(operation_char == "+"):
        result = num1 + num2
    elif(operation_char == "-"):
        result = num1 - num2
    elif(operation_char == "/"):
        result = num1 / num2
    elif(operation_char == "*"):
        result = num1 * num2
    else:
        print("Такой операции не существует")

    print("Результат операции:", result)