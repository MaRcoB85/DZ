# варіант 1
string = str(input("Enter a string: "))
string2 = string[:: -1]
if string.upper().strip() == string2.upper().strip():
    print(f'"{string}" # True')
else:
    print(f'"{string}" # False')

# варіант 2
string = str(input("Enter a string: "))
string2 = string[:: -1].upper().strip()
for index, item in enumerate(string.upper().strip()):
    if string2[index] != item:
        print(f'"{string}" # False')
        break
else:
    print(f'"{string}" # True')

