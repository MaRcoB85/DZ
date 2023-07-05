lst = [0, 5, 4, -1, 2]
min_number = int(input("Enter min number: "))
max_number = int(input("Enter max number: "))
if min_number > max_number:
    print("Error")
lst2 = [i for i in lst if min_number <= i <= max_number]
number = 1
for i in lst2:
    number = number * i
if number == 1:
    print("sum = 0, product = 0")
else:
    print(f"sum = {sum(lst2)}, product = {number}")
