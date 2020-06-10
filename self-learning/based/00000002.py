# args = ["script.py", "1", "2", "3", "4"]
# my_list = [int(x) for i, x in enumerate(args) if i > 0]
# print(str(my_list))

vowels = 'aeiou'
text = input()
for i in text:
    if i in vowels:
        print("vowel")
    elif i not in vowels and i.isalpha():
        print("consonant")
    elif not i.isalpha():
        break    
