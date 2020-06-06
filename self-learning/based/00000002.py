args = ["script.py", "1", "2", "3", "4"]
my_list = [int(x) for i, x in enumerate(args) if i > 0]
print(str(my_list))