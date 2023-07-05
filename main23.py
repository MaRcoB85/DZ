def to_dict(lst):
    if len(lst) % 2 != 0:
        lst = lst[:-1]  # відкидаємо останній елемент, якщо список складається з непарної кількості ел.
    d = {}
    for i in range(0, len(lst), 2):
        d[lst[i]] = lst[i+1]
    return d


print(to_dict([1, 2, 3, 4, 0, 6, -5, "St", 5, [1, 2]]))
