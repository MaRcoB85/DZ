# file = open('dz21.txt', 'w')

# read file
with open('dz21.txt', 'r') as file:
    lines = file.readlines()

# create dict
users = []
for line in lines:
    line.split(";")
    users.append(line)

import json
result = []
for i in users:
    fields = i.strip().split(';')
    name = fields[0].strip()
    if len(fields) >= 2 and fields[1].strip().isdigit():
        age = int(fields[1].strip())
    else:
        age = None
    phones = [phone.strip() for phone in fields[2].split(',') if phone.strip()] if len(fields) == 3 else []
    if name:
        result.append({'name': name, 'age': age, 'phones': phones})
print(result)

# json
with open('result.json', "w") as f:
    json.dump(result, f)

# out-file
with open('out_file.txt', "w") as f:
    for user in result:
        name = user['name'] if user['name'] else ''
        age = str(user['age']) if user['age'] else ''
        phones = ','.join([str(phone) for phone in user['phones']]) if user['phones'] else ''
        if name or age or phones:
            f.write(';'.join([name, age, phones]))
            f.write('\n')
