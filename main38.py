def cache_data(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if (args, tuple(kwargs.items())) in cache:
            return cache[args, tuple(kwargs.items())]
        else:
            result = func(*args, **kwargs)
            cache[args, tuple(kwargs.items())] = result
            return result

    return wrapper


@cache_data
def func_with_kwargs(title, **kwargs):
    print(f"Calculated for {title} {kwargs}")
    return sum([kwargs[key] for key in kwargs])


print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', a=100, b=4))
print(func_with_kwargs('second', a=100, b=4))
