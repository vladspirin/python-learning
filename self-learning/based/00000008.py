# def tallest_people(**user_data):
#     for key, value in sorted(user_data.items()):
#         if max(user_data.values()) == value:
#             print(key, value, sep=' : ')

    
# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)

def calculate_linear(k, b, x):
    return k * x + b


def calculate_quadratic(a, b, c, x):
    return (a * x * x) + (b * x) + c


def common_part(action):
    return print("Value of the function equals", action)


common_part(calculate_quadratic(4, 5, 6, 7))
common_part(calculate_linear(4, 5, 6))