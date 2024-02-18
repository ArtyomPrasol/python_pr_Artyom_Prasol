file_nameA = "27-169a.txt"
file_nameB = "27-169b.txt"

def count_pair_from_file(file_name):
    s = 0
    file_in = open(file_name)
    count_k, max_n = file_in.readline().split()
    mas_num = []
    for line in file_in: mas_num.append(int(line))
    for i in range(0, int(count_k)-1):
        for j in range(i, int(count_k)):
            if(int(max_n)<mas_num[i]+mas_num[j]): 
                s += 1
                print(s)
    return s

print("A: ",count_pair_from_file(file_nameA), " ; B: ", count_pair_from_file(file_nameB))