l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['John', 'Michel', 'Sunny']
# print(names[2])
# print(l[3])
# print(l[4][0])
# print(l[0:3])

l[2] = 'world'
# l[:2] = [10, 15]
l.append('new')
l.extend([5, 7])
# print(l)
l2 = ['hi', 19]
l += l2
l.insert(1, 'test')

# l.remove('world')
# el = l.pop(1)

# print(l, l.count('test'))
# только для однотипных сравнений
# l.sort()
l3 = ['hello', 'hi', 'David', 'world', 'test']
l3.sort()
print(l, l.count('test'), l3, sep='\n')

#next17