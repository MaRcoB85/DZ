lst = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]
columns = len(lst[0])
new_lst = [[] for i in range(columns)]
for i in range(columns):
    for j in range(len(lst)):
        new_lst[i].append(lst[j][i])
        new_lst[i].sort()

columns2 = len(new_lst[0])
final_lst = [[] for i in range(columns2)]
for i in range(columns2):
    for j in range(len(new_lst)):
        final_lst[i].append(new_lst[j][i])
print(final_lst)
