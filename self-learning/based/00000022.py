import itertools


main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

menu_iterator = itertools.chain(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks))
price_iterator = itertools.product(price_main_courses, price_desserts, price_drinks)
# choice_price = [i for i in price_iterator if sum(i) <= 30] 
choice_price = list(filter(lambda x: sum(x) <= 30, price_iterator))
print(choice_price)
for dish, price in menu_iterator:
    if price in choice_price:
        print(dish, price)

# choice = 

# in process

# Next

# duration = int(input())
# total_food_per_day = int(input())
# one_way_flight = int(input())
# hotel = int(input())

# print(((total_food_per_day * duration) + hotel * (duration - 1)) + one_way_flight * 2)