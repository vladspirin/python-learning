# l = [1, 2, 3, 'hello', ['test, 10'], 'world', True]
# l2 = list('hello')
# l3 = list((1, 2, 3))
# # list generator
# l4 = [i for i in 'hello']
# # l5 = [i for i in 'hello world' if i != ' ' and i !='e']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]

# print(l, l2, l3, l4, l5, sep='\n')

# range

# l6 = list(range(1, 11))
# print(l6)

for i in range(1, 3):
    print(f'Внешний цикл #{i}')
    for j in range(1, 3):
        print(f'\tВнутренний цикл #{j}')

# HW таблица умножения в консоли
