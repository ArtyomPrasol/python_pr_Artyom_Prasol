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

def sort_len_words(x):
    words = x.split()
    words.sort(key=len)
    return " ".join(words)

var = int(input("Введите 1, 2 или 3, чтоб выбрать соответствующие функции (задачи 5,7,14): "))
a = input("Введите строку: ")
match var:
    case 1:
        print(random_str(a))
    case 2: 
        print(pal_up_true(a))
    case 3:
        print(sort_len_words(a))
    case _:
        print("Вы не выбрали функцию")
