import random

lst = [random.randint(1, 100) for i in range(0,20)]
print(lst)

for i in lst:
    if lst.count(i) > 1:
        lst.remove(i)

print(lst)
print(20, len(lst))