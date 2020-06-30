# There's a function blackbox(lst) that takes a list, does some magic, and returns a list. 
# You don't know if it modifies the given list or creates a completely different one.
# Find this out testing the function on your own list and print "modifies" if the fu

# blackbox(lst)
# print("modifies")
# if the function changes the given list or "new" 
# if the returned list is not connected to the initial one.

football_list = ["Liverpool Football Club", "English Premier League", "Champion 2019-2020"]
football_list_id = id(football_list)
new_list = blackbox(football_list)
new_list_id = id(new_list)
if football_list_id == new_list_id:
    print("modifies")
else:
    print("new")
