import random
from random import randint

n = int(input("Enter number of numbers: "))
type = int(input("Enter type of entering elements (1 - manually, 2 - generate random:"))

i = 0
s = 0.0


while i<n:
    a = 0
    if type == 1:
        a = float(input("Enter number: "))
    else:
        a = randint(-100, 100)
    print(a)
    if a < 0:
        continue
    i += 1
    s += a

print(s/n)
