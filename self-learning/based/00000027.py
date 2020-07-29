def check_email(string):
    if " " in string or "@" not in string or "@." in string:
        return False
    if string.rfind(".") > string.rfind("@"):
        return True
    return False

print(check_email('good.email@example.com'))

with open('salary.txt', 'r', encoding='utf-8') as file1, open('salary_year.txt', 'w', encoding='utf-8') as file2:
    salary = file1.readlines()
    for i in salary:
        file2.write(str(int(i) * 12) + '\n')

# H/W
n = int(input())
counter = 1
lst = []
while counter <= n:
    lst.append(input().split())
    counter += 1
count = 0
new_lst = []
for i in lst:
    if 'win' in i:
        new_lst.append(i[0])
        count += 1
        
print(new_lst)
print(count)
