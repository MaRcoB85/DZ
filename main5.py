a = int(input("enter number a: ")) #за умовою число
b = int(input("enter number b: ")) #за умовою число
c = int(input("enter number c: ")) #за умовою число
if a >= b and a >= c:
    print("max number is", a)
elif b >= a and b >= c:
    print("max number is", b)
else:
    print("max number is", c)


