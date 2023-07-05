import re


def generate_sentence(text):
    pattern = r"[A-Z][^\.!?]*"
    result = re.findall(pattern, text)
    first_words = []
    for i in result:
        i = i.split()[0]
        first_words.append(i)
    last_version = ' '.join(first_words).capitalize()
    return f'"{last_version}."'


text = """
Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""

print(generate_sentence(text))
