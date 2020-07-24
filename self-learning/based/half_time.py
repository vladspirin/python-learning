N = int(input())
R = int(input())
T = 0
while N > R:
    T += 12
    N = N // 2

print(T)