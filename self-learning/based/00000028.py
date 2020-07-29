from sympy import *

n = abs(int(input()))
if isprime(n):
    print('This number is prime')
else:
    print('This number is not prime')