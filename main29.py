def linearize_list(lst):
    lst2 = []
    for i in lst:
        if isinstance(i, list):
            lst2.extend(linearize_list(i))
        else:
            lst2.append(i)
    return lst2


lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
print(linearize_list(lst))
