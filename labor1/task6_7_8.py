def kir_find_max(x):
    import re
    pat_split = "[^а-яА-Я]"
    posled = re.split(pat_split, x)
    max_posled = ""
    for i in posled:
        if(len(i)>len(max_posled)):
            max_posled = i 
    return max_posled

inputA = input("Введите строку: ")
print(kir_find_max(inputA))