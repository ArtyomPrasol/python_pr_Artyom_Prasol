def sort_mid_weigt(x):
    mas_weight = []
    for stri in x:
        weight = 0
        for ch in str(stri):
            weight += ord(ch)
        mas_weight.append(int(weight)/int(len(stri)))

    mas_weight,x = zip(*sorted(zip(mas_weight, x)))
    return x

n = input("Введите количество строк: ")
list_str = []
for i in range(int(n)):
    print(i+1)
    strok = input("Введите строку: ")
    list_str.append(strok)
print(sort_mid_weigt(list_str))