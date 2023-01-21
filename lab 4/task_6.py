n = int(input("Podaj liczbe "))
i = 2
s = 1
print(1)
while i * i <= n:
    if n % i == 0:
        print(i)
        s += i
        if i != n // i:
            s += n // i
            print(n // i)
    i += 1

if n == s:
    print("Doskonała")
else:
    print("Nie doskonała")