n = int(input("Введите количество чисел в списке: "))
mas = []

for _ in range(n):
    mas.append(int(input("Введите число: ")))

discord = {}
for i in mas:
    if(discord.get(i)==None):
        discord[i] = 1

s = 0
for i in discord:
    s += discord[i]
print("Количество чисел: ", s) 