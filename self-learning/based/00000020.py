# try:
#     name, surname = input().split()
# except ValueError:
#     print("You need to enter exactly 2 words. Try again!")
# finally:
#     print(f"Welcome to our party, {name} {surname}")


# lst = []
# for x, y in zip(input(), input()):
#     lst.append(x + y)
# print(''.join(lst))

# the following line creates a list from the input, do not modify it, please
prices = [float(price) for price in input().split()]

# your code below
for i, price in enumerate(prices):
    if price.is_integer():
        prices[i] = int(price)
print(sorted(prices, reverse=True))