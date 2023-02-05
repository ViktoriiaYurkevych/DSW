import random

a = [random.randint(1, 100) for i in range(100)]
b = random.sample(a, len(a))

print(a)
print("Shuffle of list: ")
print(b)

print(sorted(a))


