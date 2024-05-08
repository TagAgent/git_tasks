
def find_season(number: int):
    """Find seson by number"""
    if number == 12 or number <= 2 and number >= 1:
        print("Зима")
    elif number >= 3 and number <= 5:
        print("Весна")
    elif number >= 6 and number <= 8:
        print("Лето")
    elif number >= 9 and number <= 11:
        print("Осень")
    else:
        print("Месяца под таким номером не существует")
