# while stmt:
#     do...
# while True:
#     print('Hello')
# i = 1
# while i <= 10:
#     print(i, end=' ')
#     # i = i + 1
#     i += 1


# for
# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(f'"{l}"', end=' ')
# else (for)
# for i in 'Helloworld':
#     if i == ' ':
#         break
#     print(i, end=' ')
# else:
#     print('\nNo spaces')
# HW
cal = 1900

while cal <= 2020:
    print(cal)
    cal += 1
else:
    print('Done')

i = 0
a = 'a'
while i < 8:
    a *= 2
    i += 1
print(a)