def find_except(x):
    for i in x:
        if(x.count(i)==1):
            return i
        

def find_two_min_elem(x):
    min = float('inf')
    for i in x:
        if (min>i):
            min = i

    count_f = min + 1
    while (True):
        if(x.count(count_f)):
            return [min, count_f]
        count_f += 1

def find_R_mas(x):
    R = int(input("Введите число для поиска: "))
    if(x.count(R)):
        return R
    up = R + 1
    down = R - 1
    while (True):
        if(x.count(up)):
            return up
        if(x.count(down)):
            return down
        up += 1
        down -= 1


n = int(input("Введите количество элементов в массиве: "))
mas =[]
for i in range(n):
    print(i+1)
    mas.append(int(input("Введите элемент: ")))
print(find_R_mas(mas))