users = [
    {'name': 'Luarvik Liya', 'age': 17},
    {'name': 'Ola Andvar', 'age': 18},
    {'name': 'Brun Du Barnstokr', 'age': 19},
    {'name': 'Musi Pusi', 'age': 13},
    {'name': 'Olga Orel', 'age': 20},
    {'name': 'Igor Puntii', 'age': 25}
]
users2 = []
for i in users:
    if i['age'] >= 18:
        users2.append(i['name'])
print(users2)
