# def concat(*string, sep=" "):
#     return sep.join(string)
# print(concat("cat", "dog"))


# def tracklist(**kwargs):
#     for key in kwargs:
#         print(key)
#         for k, v in kwargs[key].items():
#             print(f"ALBUM: {k} TRACK: {v}")

# tracklist(Woodkid={"The Golden Age": "Run Boy Run", "On the Other Side": "Samara"},\
#           Cure={"Disintegration": "Lovesong", "Wish": "Friday I'm in love", "Seventeen Seconds": "A Forest"},\
#           Placebo={"Sleeping with Ghosts": "Protect Me From What I Want"})
    
# def print_book_info(title, author=None, year=None):
#     if author is not None and year is not None:
#         print(title)
#     elif author is None and year is not None:
#         print(f"{title}, was written by {author}")
#     elif author is not None and year is None:
#         print(f"{title}, was written in {year}")
#     else:
#         print(f"{title}, was written by {author} in {year}")

# print_book_info("Crime and Punishment", "Leo", 1866)

# def average_mark(*test_score):
#     return round(sum(test_score) / len(test_score), 1)

# print(average_mark(3, 4, 5, 3))

transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
transaction_dict = dict()
for account_id, transaction in transactions:
    transaction_dict.setdefault(account_id, []).append(transaction)
transaction_dict = {key: [sum(value)] for key, value in transaction_dict.items()}
print(transaction_dict)
