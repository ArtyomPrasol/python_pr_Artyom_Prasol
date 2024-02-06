def sort_mid_weigt(x):
    mas_weight = []
    for stri in x:
        weight = 0
        for ch in str(stri):
            weight += ord(ch)
        mas_weight.append(int(weight)/int(len(stri)))

    mas_weight,x = zip(*sorted(zip(mas_weight, x)))
    return x

def func3(x):
    mas_razn = []
    
    for stri in x:
        razn = 0
        max_ord = 0
        for ch in stri:
            if(max_ord<ord(ch)):
                max_ord = ord(ch)
        for i in range(int(len(stri)/2)):
            count = 0
            if(ord(stri[i])==ord(stri[len(stri)-i-1])):
                count += 1
                razn += (ord(stri[i])-max_ord)**2
        mas_razn.append((razn/count)**(1/2))

    mas_razn, x = zip(*sorted(zip(mas_razn,x)))
    return x


def func4(x):
    all_str = ""
    for stri in x:
        all_str += stri

    count_all = len(all_str)
    max_ch = ""
    max_count = 0
    
    while (all_str!=""):
        count = all_str.count(all_str[0])
        if(max_count<count):
            max_ch = all_str[0]
            max_count = count
        all_str = all_str.replace(all_str[0],"")

    mas_razn = []
    max_frq = max_count/count_all
    for stri in x:
        mas_razn.append(stri.count(max_ch)/len(stri)-max_frq)

    mas_razn, x = zip(*sorted(zip(mas_razn,x)))
    return x


n = input("Введите количество строк: ")
list_str = []
for i in range(int(n)):
    print(i+1)
    strok = input("Введите строку: ")
    list_str.append(strok)
print(func4(list_str))