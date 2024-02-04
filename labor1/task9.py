n = input("Введите количество строк: ")
list_str = []
for i in range(int(n)):
    print(i+1)
    strok = input("Введите строку: ")
    list_str.append(strok)
list_str.sort(key=len)
print(list_str)