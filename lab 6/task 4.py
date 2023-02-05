def get_divisors(n):
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            yield i
    yield n

k = int(input("Enter number:"))
print(list(k for k in get_divisors(k)))
