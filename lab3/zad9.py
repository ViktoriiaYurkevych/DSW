import random
a = [i for i in range(1, 91)]
random.shuffle(a)
print(*a[:5])