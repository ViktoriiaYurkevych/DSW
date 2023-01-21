flag = True

n = int(input("Podaj liczbe: "))

while flag:
    k = n
    n = int(input("Podaj liczbe: "))
    if abs(n - k) < 5:
        flag = False