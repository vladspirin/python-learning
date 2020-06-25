# def final_deposit_amount(*interest, amount=1000):
#     for i in interest:
#         amount = amount * (1 + i/100)
#     return round(amount, 2)
# print(final_deposit_amount(5, 7, 4))

def tallest_people(**user_data):
    max_key = max(user_data, key=user_data.get)
    max_value = max(user_data.values())
    # srt_list = sorted(user_data)
    # print(srt_list)
    for key, value in user_data.items():
        if max_value == value:
            return print(max_key, max_value, sep=' : ')
    
tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)