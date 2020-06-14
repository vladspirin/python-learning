# 1.
list_1 = [1, 2, 3]
list_2 = [i * 2 for i in list_1]
print(list_2)
# 2.
list_1 = [1, 2, 3]
list_2 = [pow(i, 2) for i in list_1]
print(sum(list_2))
# 3.
timer = float(input())
result = int(timer * 0.5)
print(result)
# 4.
txt = 'Hello world'
if not txt.isalpha():
    txt = txt.upper()
else:
    txt = txt.lower()
print(txt)

# Next topic №19