# meals = [
#         {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#         {"title": "Italian salad with fusilli and ham", "kcal": 320},
#         {"title": "Bulgur with vegetables", "kcal": 350},
#         {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#         {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

# print(sum([i.get("kcal") for i in meals]))
# kcal = 0
# for i in meals:
#     kcal += i["kcal"]
# print(kcal)


from collections import defaultdict

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

number = int(input())
txt_list = text.split()
freq_counter = Counter(txt_list)
my_dict = dict(freq_counter.most_common(number))
for k, v in my_dict.items():
    print(k, v)


transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]
# transactions.reverse()
# create transaction_dict
transaction_dict = {key: list(key) for key in transactions}
for value in transaction_dict.values():
    del value[0]
# for key, value in transaction_dict.items():
#     if key[0] == key[0] + 1:
#         value = (key[1] + value[1])
#     print(value)
    

# transaction_dict = defaultdict(transactions[0])
print(transaction_dict)

def congratulations(pm, tester, *names):
    print(f"Happy New Year! Take care of yourself and your loved ones!\nFor:\n {pm}\n {tester}")
    for name in names:
        print(name)
congratulations("Alice", "Mike", "Denis", "Joey")


test_dict = {"a": 43, "b": 1233, "c": 8}
for k, v in test_dict.items():
    if v == min(test_dict.values()):
        print(f'min: {k}')

for k, v in test_dict.items():
    if v == max(test_dict.values()):
        print(f'max: {k}')
