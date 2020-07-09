# one_cup = {'water': 200, 'milk': 50, 'coffee_beans': 15}
# # amt = {}


# # def gather_to_dict(**kwargs):
# #     global amt
# #     amt.update(kwargs.items()) 
# #     return print(amt)


# # gather_to_dict(water=int(input('Write how many cups of coffee you will need:\n')),
# #             milk=int(input('Write how many ml of milk the coffee machine has:\n')),
# #             coffee_beans=int(input('Write how many grams of coffee beans the coffee machine has:\n')))


# water = int(input('Write how many cups of coffee you will need:\n'))
# milk = int(input('Write how many ml of milk the coffee machine has:\n'))
# coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
# N_cups = abs(int(input('Write how many cups of coffee you will need:\n')))

# def cups_count(cup):
#     amount = int(
#         ((one_cup.get('water') * N_cups) + (one_cup.get('milk') * N_cups) + (one_cup.get('coffee_beans') * N_cups))
#         / sum(one_cup.values()))
#     return print(amount)


# cups_count(N_cups)


one_cup = {'water': 200, 'milk': 50, 'coffee_beans': 15}

water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has:\n'))
coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
N_cups = abs(int(input('Write how many cups of coffee you will need:\n')))


def cups_count():
    return int((one_cup.get('water') * N_cups + one_cup.get('milk') * N_cups
                + one_cup.get('coffee_beans') * N_cups) / sum(one_cup.values()))


def check_items():
    water_amt = int(water / one_cup.get('water'))
    milk_amt = int(milk / one_cup.get('milk'))
    cof_amt = int(coffee_beans / one_cup.get('coffee_beans'))
    amt_average = min([water_amt, milk_amt, cof_amt])
    if N_cups == 1 or N_cups == 0:
        if one_cup.get('water') <= water:
            if one_cup.get('milk') <= milk:
                if one_cup.get('coffee_beans') <= coffee_beans:
                    return print('Yes, I can make that amount of coffee')
    elif N_cups > 1:
        if one_cup.get('water') < water:
            if one_cup.get('milk') < milk:
                if one_cup.get('coffee_beans') < coffee_beans:
                    return print(f'Yes, I can make that amount of coffee {amt_average - cups_count()} more than that')
                return print(f'No, I can make only {cups_count()} cups of coffee')


check_items()
