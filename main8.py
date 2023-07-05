a = int(input("Enter minimal width: "))
b = int(input("Enter maximal width: "))
if a > b or a <= 0 or b <= 0:
    print("It is impossible")
elif (b-a) % 2:
    print("Need to be difference like an even number")
else:
    print(" " * ((b - a)//2) + "*" * a)
    for i in range(a+1, b+1, 2):
        print(" " * ((b - i)//2) + "*" + " " * (i-1) + "*")
    for i in range(b-3, a-1, -2):
        print(" " * ((b - i)//2) + "*" + " " * (i-1) + "*")
    print(" " * ((b - a) // 2) + "*" * a)
