def deep(x):
    if x not in tree:
        return 0
    else:
        return 1 + deep(tree[x])

tree = {}
n = int(input("Введите количество элементов в древе: "))
for i in range(n-1):
    ch, par = input("Введите ребенка и родителя: ").split()
    tree[ch] = par

mas_d = {}
for i in set(tree.keys()).union(set(tree.values())):
    mas_d[i] = deep(i)

for key, value in sorted(mas_d.items()):
    print(key, value)