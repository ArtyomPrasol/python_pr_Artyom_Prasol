import random

def random_str(x):
    char = list(x)
    random.shuffle(char)
    y = "".join(char)
    return y



var = int(input("Введите 1, 2 или 3, чтоб выбрать соответствующие функции (5,7,14): "))
a = input("Введите строку: ")
match var:
    case 1:
        print(random_str(a))
    case _:
        print("Вы не выбрали функцию")
