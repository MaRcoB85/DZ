a = int(input("Enter size of triangle: "))
for i in range(1, a+1):
    if i < a:
        print(" "*(a-i-1), "*" * i)
    else:
        print("*" * i)
