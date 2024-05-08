
def chek_is_number_easy(number: int):
    counter = 0
    for i in range(2, number):
        if(number % i == 0):
            counter += 1
    if(counter == 0):
        print("Число простое")
    else:
        print("Число не простое")