# просто декоратор
def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


@italic_decorator
def greetings(name, cat):
    return f"Hello, {name} and {cat}"


print(greetings("Anna", "Murzik"))

# декоратор з параметром (передаємо, що хочемо зробити і викликається потрібна функція)
def style_decorator(style):
    def param_decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{style}>{func(*args, **kwargs)}</{style}>"
        return wrapper
    return param_decorator


@style_decorator('i')
@style_decorator('b')
def greetings(name, cat):
    return f"Hello, {name} and {cat}"

print(greetings("Anna", "Murzik"))