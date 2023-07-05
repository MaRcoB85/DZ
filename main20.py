with open('data.txt', 'r') as file:
    max_line = ''
    max_len = 0
    for line in file:
        if len(line) > max_len:
            max_len = len(line)
            max_line = line
print(f"The longest line is: {max_line}")
