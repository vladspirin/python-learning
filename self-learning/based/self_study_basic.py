print('Hello, World!')
# однострочный комментарий
'''
Это
многострочный
комменатрий ,но это и строка
'''

"""
Это
многострочный
комменатрий
"""
# 1. Арифметические операторы
print(2 + 3) # 5
print(10 - 3) # 7
print(10 * 3) # 30
print(10 / 2) # 5.0
print(2**3) # 8
print(10 // 3) # 3
print(-5 - 3) # -8
print(100 ** 0.5) # 10.0

# можно всё комбинировать

print(2 + 3 * 4) # 14
print( (2 + 3) * 4) # 20

print(0.5 + 2) # 2.5
print(0.1 + 0.2) # 0.30000000000000004

# 2. Переменные
x = 1
y = 5
my_vbar1 = 50
_myvar1 = 100

# Python язык динамической типизации

print(type(x))

# переменные в Python являются регистрозависимыми

TEST = 20 # псевдоконстанта , в Python констант нет, но есть соглашение если так определяется что это то же, что и константа


test = None # None это отсутствие значения
print(test)

print(x, y)

# a, b = (3, 4)
# print(a, b)

# 3. Булевый тип данных

my_true = True
my_false = False

print(type(my_true))
print(type(my_false))

# str() int() float() bool() - конструкторы (функции) которые приводят значения к указаному типу

x = 5.2
print(x, type(x))
x = int(x)
print(x, type(x))

x = bool(x)
print(x, type(x))