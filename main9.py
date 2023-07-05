a = int(input("Enter n: "))
if a < 0:
    print("Enter a positive number")
if a == 0:
    print(a)
for i in range(1, a+1):
    for j in range(a-i):
        print(" " * 2, end="")
    for j in range(1, i):
        print(j, end=" ")
    for j in range(i, 0, -1):
        if j == 1:
            print("1")
        else:
            print(j, end=" ")
