def get_percentage(number, ndigits=None):
    result = round((float(number) * 100), ndigits)
    return print(f'{result}%')

get_percentage(0.0123)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(numbers[5:101:5])

# Imagine, there are three children in a family and they wrote down who they want to be when they grow up:

# children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
# Let's say you want to store not only the profession they have chosen, but also their age: Emily is 5, Adam is 9, and Nancy is 14.
#  To do so, you can create nested dictionaries for each key in the outer dictionary.

# For each name, create a nested dictionary with the keys 'profession' and 'age', modify the dictionary children but don't print it.

# NB: write the age as an integer.


children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
age = {'Emily': 5, 'Adam': 9, 'Nancy': 14}
children = {key: {'profession': children.get(key), 'age': age.get(key)} for key in children}

# In a farming game, you can buy certain animals for a specific price. As a player, you want to buy the most useful (i.e. the most expensive) animal. Here are the animals and their prices:
# Item: Price
# Chicken: 23
# Goat: 678
# Pig: 1296
# Cow: 3848
# Sheep: 6769
# Write a program that determines what is the most expensive animal that the user can buy with their money and how many of them they can buy.
# The input format:
# The money that the user has.
# The output format:
# How many animals the user can afford, for example, 20 chickens or 4 cows. If the user cannot afford any animal, write None. 
# Pay attention to the number of nouns. Also, keep in mind that the word "sheep" has the irregular plural form "sheep".

animals_cost = {'chicken': 23, 'goat': 678, 'pig': 1296, 'cow': 3848, 'sheep': 6769}
for value in animals_cost:
    cost = animals_cost[value]

user_money = int(input())

def animal_calc(money, animal):
    if money < animal:
        return print(None)
    first_result = money // animal
    last_result = money % animal
    if last_result == 0 or last_result < 23: 
        return first_result
    # elif last_result in animals_cost:
    #     last_result = last_result // animal
    else:
        return first_result, last_result

print(animal_calc(user_money, cost))