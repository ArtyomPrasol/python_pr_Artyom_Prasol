def find_except(x):
    for i in x:
        if(x.count(i)==1):
            return i

n = int(input("Введите количество элементов в массиве: "))
mas =[]
for i in range(n):
    print(i+1)
    mas.append(int(input("Введите элемент: ")))
print(find_except(mas))