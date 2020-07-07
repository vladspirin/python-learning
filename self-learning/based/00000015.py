# import random

# random.seed(3)
# print(random.betavariate(0.9, 0.1))

word = "python"

def letters(word):
    for i in word:
        yield i

# word = input()
# print(word[1::2])

prime_numbers = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n - 1))]
# print(prime_numbers)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pow_num_list = list(map(lambda x: x ** 2, numbers))
# print(pow_num_list)
odd_numbers = list(filter(lambda x: x % 2, numbers))
# print(odd_numbers)
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_product(list_1, list_2):
    return list(map(lambda x, y: x * y, list_1, list_2))

# print(my_product(numbers, numbers_2))

even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# length = len(even)

# my_sum = []
# i = 0
# while i < length:
#     my_sum.append(even[i] + odd[i])
#     i = i + 1

# print(my_sum)
# remainders = [x % 3 for x in my_sum]
# print(remainders)
# nonzero_remainders = [r for r in remainders if r]
# print(nonzero_remainders)

my_sum = list(map(lambda x, y: x + y, even, odd))
print(my_sum)
remainders = list(map(lambda x: x % 3, my_sum))
print(remainders)
nonzero_remainders = list(filter(lambda x: x, remainders))
print(nonzero_remainders)

