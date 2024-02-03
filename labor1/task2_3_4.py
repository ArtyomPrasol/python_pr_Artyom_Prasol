import random

def random_str(x):
    char = list(x)
    random.shuffle(char)
    y = "".join(char)
    return y

def pal_up_true(x):
    for char in str(x):
        if(char.isdigit()):
            return "В строке есть числа"
    y = ""
    for char in str(x):
        if(char.isupper()):
            y += str(char)
    if (y == y[::-1]):
        return "Палиндром"
    else:
        return "Не палиндром"

var = int(input("Введите 1, 2 или 3, чтоб выбрать соответствующие функции (5,7,14): "))
a = input("Введите строку: ")
match var:
    case 1:
        print(random_str(a))
    case 2: 
        print(pal_up_true(a))
    case _:
        print("Вы не выбрали функцию")
