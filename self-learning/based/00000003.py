# movie (dir. director) came out in year
# movie = input()
# director = input()
# year = input()
# print(f'{movie} (dir. {director}) came out in {year}')

# txt = input()
# txt = txt.title()
# for i in txt:
#     if not i.isalpha():
#         txt = txt.replace(i, "")
             
# print(txt)

def heading(string, number=1):
    for i in range(1, 7):
        if number == i:
            return print(("#" * i) + " " + string)
        elif number < i:
            return print(("#" * 1) + " " + string)
        elif number > i:
            return print(("#" * 6) + " " + string)
       

