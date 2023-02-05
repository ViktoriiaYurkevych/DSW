s = 0
for i in range(1, 100):
    s += i ** 3

print("sumę sześcianów liczb: ", s)

sum = 0
k = 0
while True:
    sum += k
    k += 1
    if sum > 10**6:
        break
    k += 1

print(k)