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


def find_all_del(x):
    mas_del = []
    for i in x:
        for j in range(1, int(i)+1):
            if(int(i) % int(j) == 0):
                if(mas_del.count(j)==0):
                    mas_del.append(j)
    return mas_del


def new_mas(x):
    mas = []
    for i in x:
        if (i>=0 and i**2<100 and x.count(i)>=2 and mas.count(i**2)==0):
            mas.append(i**2)
    return mas
            


n = int(input("Введите количество элементов в массиве: "))
mas =[]
for i in range(n):
    print(i+1)
    mas.append(int(input("Введите элемент: ")))
print(new_mas(mas))