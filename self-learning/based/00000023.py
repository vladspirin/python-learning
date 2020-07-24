# from collections import ChainMap

# food_types = {'Vegetables': 15, 'Dairy': 20, 'Meat': 3, 'Cereals': 9, 'Fruits': 11, 'Fish': 7}
# countries = {'USA': 25, 'Australia': 15, 'Canada': 15, 'France': 6, 'India': 4}
# discount = {'gold': 20, 'regular': 10}

# chain = ChainMap(food_types, countries)
# food_types['Sweets'] = 10

# # some missing lines
# countries['USA'] = 35
# chain = chain.new_child(discount)
# print(chain)


# def range_sum(numbers, start, end):
#     return sum([x for x in numbers if start <= x <= end])


# input_numbers = [int(i) for i in input().split()]
# a, b = map(int, input().split())
# print(range_sum(input_numbers, a, b))


# passwords = input().split()
# # passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']
# passwords.sort(key=len)
# for i in passwords:
#     print(i, len(i))

from datetime import datetime


def get_weekday(datetime_obj):
    d = datetime.strptime(datetime_obj, "%Y-%m-%d")
    return d.strftime("%A")

print(get_weekday('2019-12-31'))

# JetBrains Academy solution

# def get_weekday(datetime_obj):
#     return datetime_obj.strftime("%A")


def get_release_date(release_str):
    s = release_str.replace("Day of release: ", "")
    release = datetime.strptime(s, "%d %B %Y")
    return release.strftime("%Y-%m-%d %H:%M:%S")

print(get_release_date("Day of release: 4 July 2019"))