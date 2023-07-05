lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lst2 = []
lst3 = []
lst4 = []
for i in lst:
    if i % 5 == 0:
        continue
    elif i % 3 == 0:
        lst2.append(i)
for i in lst:
    if i % 3 == 0:
        continue
    elif i % 5 == 0:
        lst3.append(i)
for i in lst:
    if i % 3 == 0 and i % 5 == 0:
        lst4.append(i)
print(lst2, " # elements divided by 3")
print(lst3, " # elements divided by 5")
print(lst4, " # elements divided by 3 and by 5")
