lst = [3.5, 2, 4, 6.2, 8]
lst2 = []
for i in range(len(lst)-1):
    lst2.append(lst[i])
    lst2.append((lst[i]+lst[i+1])/2)
lst2.append(lst[-1])
print(lst2)
