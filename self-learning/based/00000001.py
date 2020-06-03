# x = input()
# y = input()

# if "." in x:
#     x = float(x)
# else:
#     x = int(x)

# if "." in y:
#     y = float(y)
# else:
#     y = int(y)

# quadrant_1 = "I"
# quadrant_2 = "II"
# quadrant_3 = "III"
# quadrant_4 = "IV"

# if x > 0 and y > 0:
#     print(quadrant_1)
# elif x < 0 < y:
#     print(quadrant_2)
# elif x < 0 > y:
#     print(quadrant_3)
# else:
#     print(quadrant_4)

# a = int(input())
# b = int(input())
# x = 0
# k = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         k += 1
#         x = (i + x)
        
# print(x / k)                 

# word_or_phrase = input()

# for letter in word_or_phrase:
#     if letter.isupper():
#         x = "_" + letter.swapcase()
#         word_or_phrase.replace(letter, x)

      
# print(word_or_phrase)
        
# print(letter)        

              
# numbers = []
# res = None
# n = int(input())
# for i in range(n):
#     # numbers.append(int(input()))
# # for x in numbers:
#     res = sum(int(input())) / len(n)    
# print(res)

# n = int(input())

# for n in range(n):
#     m = int(input())
#     if m % 7 == 0:
#         m *= m
#         print(m)

# first_list = [int(x) for x in input()]
# second_list = [sum(first_list[:n]) for n in range(1, len(first_list) + 1)]

# print(second_list)
# matrix = [[j for j in range(5)] for i in range(2)]
# print(matrix)

# my_list = [[j for j in range(1, 3)] for i in range(5)]
# print(my_list)

# str_1 = input()
# str_2 = input()
# str_3 = input()

# my_list = [str_1 for i in range(1) for str_2 in range(1) for str_3 in range(2)]
# my_list = []
# for i in range(1):
#     my_list.append(str_1)
#     for j in range(1):
#         my_list.append([str_2])
#         for k in range(1):
#             my_list.append([[str_3]])

# print(my_list)

# text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
#         ["Ephemeral", "lasts", "one", "day", "only"],
#         ["Accolade", "is", "an", "expression", "of", "praise"]]
# txt = int(input())
# new_list = []
# for i in text:
#     for j in i:
#         if txt >= len(j):
#             new_list.append(j)     
# print(new_list)

# for i in user_turn:
#     # print(i)
#     if i == line_1:
#         print("X wins")

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


# A[i] = (x[i] + x[i + 1]) / 2

# numbers = [int(i) for i in input()]
# result_list = []
# def sum_next_el(el):
#     result = numbers[0] + numbers[1]
#     result_list.append(result / 2)
#     del numbers[0]
#     result = numbers[0] + numbers[1]
#     result_list.append(result / 2)
#     del numbers[0]
#     result = numbers[0] + numbers[1]
#     result_list.append(result / 2)
#     del numbers[0]
#     result = numbers[0] + numbers[1]
#     result_list.append(result / 2)
#     del numbers[0]
#     return result

# sum_next_el(numbers)
# print(result_list)

# random_numbers = [1, 22, 333, 4444, 55555]
# random_numbers = [str(i) for i in random_numbers]
# print("\n".join(random_numbers))


# total = 0
# count = 0

# while True:
#     n = input()
#     if n == '.':
#         break
#     total += int(n)
#     count += 1

# print(total / count)

# dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
#               'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
#               'sign', 'the', 'to', 'uncertain']
# sentence = input().lower()
# for i in dictionary:
#     for j in sentence:
#         if i == j:
#             print("OK")
# total = []
# count = 0

# while True:
#     n = input()
#     if n == '.':
#         break
#     total.append(float(n))
#     count += 1

# print(min(total))

# x, y = input().split()
# print(f"{x} of {y}")

# scores = input().split()
# # put your python code here
# for i in scores:
#     if scores.count("I") == 3:
#         print("Game over")
#         print(scores.count("C"))
#         break    
#     else:
#         print("You won")
#         print(scores.count("C"))
#         break
# print(scores)

scores = input().split()
counter = 0
i = 0
while True:
    if scores[i] == str():
        counter += 1
    if scores.count("I") == 3:
        print("Game over")
        break
    
    print(counter) 