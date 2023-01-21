print("równanie kwadratowe: ax2 + bx + c ")
a = float(input("Podaj liczbę: "))
b = float(input("Podaj liczbę: "))
c = float(input("Podaj liczbę: "))
d = float(input("Podaj liczbę: "))
discr = b**2 + 4 * a * c

print('discr = ' + str(discr))
if discr < 0 :
    print("bez")
elif discr == 0:
    x = -b / (2 * a)
    print(" x = " + str(x))
else:
    x1 = (-b + discr ** 0.5) / ( 2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
