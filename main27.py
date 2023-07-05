def gen_func(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            yield j**i


generator = gen_func(3, 4)
result = ' '.join(str(x) for x in generator)
print(result)

# краще так
def gen_func(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            yield j**i

result = ' '.join(str(x) for x in gen_func(3, 4))
print(result)