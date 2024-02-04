def kir_find_max(x):
    pat = r'[а-яА-Я]+'
    listX = x.find(pat)
    return listX

inputA = input("Введите строку: ")
print(kir_find_max(inputA))