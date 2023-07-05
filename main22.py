def read_last(file_path, symbol_number):
    pass
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            last_symbols = line[-symbol_number-1:]
            if line.strip():
                print(last_symbols.strip())


file_path = 'C:\\Users\\Marina Koba\\Downloads\\read_last.txt'


read_last(file_path, 8)
