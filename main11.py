multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
words = multi_string.split(" .") and multi_string.split(".")
words_number = []
for i in words:
    a = i.split()
    quantity = len(a)
    if len(a) < 1:
        continue
    words_number.append(quantity)
print("words_number ->", words_number)
