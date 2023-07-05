import random


def generate_random_string(length):
    result = ''
    for i in range(length):
        random_num = random.randint(48, 122)
        while not (48 <= random_num <= 57 or 65 <= random_num <= 90 or 97 <= random_num <= 122):
            random_num = random.randint(48, 122)
        result += chr(random_num)
    return result


print(generate_random_string(12))
