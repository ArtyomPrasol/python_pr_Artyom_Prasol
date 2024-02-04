def kir_in_find_max(x):
    import re
    pat_split = "[^а-яА-Я]"
    posled = re.split(pat_split, x)
    max_posled = ""
    for i in posled:
        if(len(i)>len(max_posled)):
            max_posled = i 
    return max_posled

def find_min_num(x):
    import re
    pat_split = "[^0-9]"
    mas = re.split(pat_split, x)
    min_num = float('inf')
    for i in mas:
        if(i!=""):
            if(int(i)<min_num):
                min_num = int(i)
    return min_num

def num_in_find_max(x):
    import re
    pat_split = "[^0-9]"
    posled = re.split(pat_split, x)
    max_posled = ""
    for i in posled:
        if(len(i)>len(max_posled)):
            max_posled = i 
    return len(max_posled)

inputA = input("Введите строку: ")
print(num_in_find_max(inputA))