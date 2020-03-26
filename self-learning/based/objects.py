# Неизменяемые типы данных
# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))

# s = 'hello'
# print(s, id(s))
# s += ' world'
# print(s, id(s))

# Изменяемые типы данных
# l = [1, 2, 3]
# print(l, id(l))
# l.append(5)
# print(l, id(l))

# x = 10
# y = x
# print(x, id(x), y, id(y))
#
# x = 15
# print(x, id(x))
# print(y, id(y))

# l1 = [1, 2, 3]
# l2 = l1
# print(l1, id(l1), l2, id(l2))
#
# l1.append((5))
# print(l1, id(l1), l2, id(l2))

# l2 = l1.copy()
# l2 - l1[:]
# print(l1, id(l1), l2, id(l2))

x = 10
print(x)
del x
# print(x)