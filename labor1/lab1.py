def count_del_not_include3(x):
    s = 0
    for i in range(1, int(x)):
        if (x%i==0):
            if (i%3!=0):
                s += 1
    return s

def min_digit(x):
    z = 10
    for i in str(x):
        if (int(i)<z and int(i)%2==1):
            z = int(i)
    return z

def func3(x):
    s = 0
    p = 1
    for i in str(x):
        s += int(i)
        p *= int(i)
    
    def check_sim(n,m):
        while n and m:
            if(n > m):
                n %= m
            else:
                m %= n
        if (n + m == 1):
            return 1
        else:
            return 0

    func_s = 0
    for i in range(1, int(x)):
        if x % i == 0:
            if (check_sim(i,s)==1 and check_sim(i,p)==0):
                func_s += i
    return func_s

a = int(input("Введите число для 1 функции: "))
print(count_del_not_include3(a))
b = int(input("Введите число для 2 функции: "))
print(min_digit(b))
c = int(input("Введите число для 3 функции: "))
print(func3(c))
