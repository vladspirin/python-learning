# names = []
# numbers = []
# while True:
#     address = input()
#     if address == "MEOW":
#         break
#     address_split = address.split()
#     names.append(address_split[0])
#     numbers.append(int(address_split[1]))

# x = numbers.index(max(numbers))
# print(names[x])


i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1

print(i)
