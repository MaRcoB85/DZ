a = str(input("Your mail: "))
if a.startswith("@"):                            #@tttt.ua
    print(f'email = "{a}"  # False')
elif a.endswith("."):                            #tttt@ttt.
    print(f'email = "{a}"  # False')
elif a.count("@") != 1 or a.count(".") != 1:     #tttt@ttt.  ttt@tt.ua.ua
    print(f'email = "{a}"  # False')
elif a.index(".") < a.index("@"):                #ttt.ua@ttt
    print(f'email = "{a}"  # False')
else:                                            #ttt@com.ua
    print(f'email = "{a}"  # True')