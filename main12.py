s = "aab qq c badcc a qqqqqaqqqqaa tpara"
a = []
for i in s.split():
    if i.count("a") == 2:
        a.append(i)
print(" ".join(a).title())
