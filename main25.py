def call_counter(filename):
    def param_counter(func):
        def wrapper(*args, **kwargs):
            wrapper.counter += 1
            with open(filename, "a") as file:
                file.write(f"Function '{func.__name__}' was called {wrapper.counter} times\n")
            return func(*args, **kwargs)
        wrapper.counter = 0
        return wrapper
    return param_counter


@call_counter('data2.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(4, 6))
print(add(4, 6))
print(add(4, 6))
