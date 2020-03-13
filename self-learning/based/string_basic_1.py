# s = 'hello'
# print(len(s))
# s2 = s.capitalize()
# print(s, s2)
# print(s.center(20, '!'))
# print(s.count('l'))

name = 'Vlad'
age = 30

# print('My name is ' + name + '. I\'m ' + str(age))

# именные маркеры
# print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age})

# позиционные маркеры
# print('My name is %s. I\'m %d' %(name, age))
# print('Title: %s, Price: %.2f' %('Sony', 40))

# метод format
# print('My name is {}. I\'m {}'.format(name, age))
# print('My name is {x}. I\'m {y}'.format(x=name, y=age))

# f-strings
# print(f'My name is {name}. I\'m {age}')
# print(f'My name is {name}. I\'m {age + 8}')
print('5  + 2 = {}'.format(5 + 2))
print(f'5  + 2 = {5 + 2}')