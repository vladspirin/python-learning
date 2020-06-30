# # 2.
# print("".join([chr(ord(i) + 1) for i in input()]))

# # 3.
# u_code = int(input())
# print(chr(u_code)) if u_code in range(32, 127) else print(False)

# # 4.
# numbers = [1, 2, 3]
# my_generator = (n ** 2 for n in numbers)
# for n in my_generator:
#     print(n)

# # 5.
# sum_gen = sum((int(i) for i in input()))

# # 6.

# n = int(input())


# def squares(num):
#     i = 1
#     while i <= num:
#         yield i ** 2
#         i += 1
    

# my_generator = squares(n)
# for j in my_generator:
#     print(j)

# 7.

n = int(input())


def even(number):
    x = 0
    while x <= (number * 2) - 1:
        if x % 2 == 0:
            yield x
        x += 1

my_generator = even(n)
for y in my_generator:
    print(y)
