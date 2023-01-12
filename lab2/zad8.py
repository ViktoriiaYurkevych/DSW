a = int(input("Podaj str: "))
b = int(input("Podaj str: "))
c = int(input("Podaj str: "))

if (a >= b and a >= c and a**2 == b**2 + c**2) or \
        (b >= a and b >= c and b**2 == a**2 + c**2) or \
        (c >= a and c >= b and c**2 == a**2 + b**2):
    print("Prost")
else:
    print("Nieprost")
