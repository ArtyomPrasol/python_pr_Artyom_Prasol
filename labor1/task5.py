def find_dates(str):
    import re
    pat = r'\d{1,2} [А-Я][а-яА-Я]+ \d{4}'
    form = re.findall(pat, str)
    return form

inputA = input("Введите строку: ")
print(find_dates(inputA))

#(Января|Февраля|Марта|Апреля|Мая|Июня|Июля|Августа|Сентября|Октября|Ноября|Декабря)