def custom_zip(*sequences, full, default='Q'):
    result = []
    if full:
        max_len = max(len(seq) for seq in sequences)
        for i in range(max_len):
            item = ()
            for num in sequences:
                if i < len(num):
                    item += (num[i],)
                else:
                    item += (default,)
            result.append(item)
    else:
        min_len = min(len(seq) for seq in sequences)
        for i in range(min_len):
            item = ()
            for num in sequences:
                item += (num[i],)
            result.append(item)
    return result


print(custom_zip([1, 2, 3, 4, 5], [9, 8, 7], full=True))
