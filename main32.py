def custom_map(func, *sequences):
    n = min(len(seq) for seq in sequences)
    if len(sequences) == 1:
        return [func(x) for x in sequences[0]]
    else:
        result = []
        for i in range(n):
            args = [seq[i] for seq in sequences]
            result.append(func(*args))
        return result


print(custom_map(sum, [[1, 2, 3], [4, 5]]))
print(custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)))
