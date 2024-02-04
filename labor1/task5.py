def find_dates(str):
    import re
    pat = r'\d{1,2} [а-я]+ \d{4}'
    form = re.findall(pat, str)
    return form

inputA = input("Введите строку: ")
print(find_dates(inputA))

#(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)