from random import randint as rand

multi_matryca = [[88],
                 [24,120],
                 [18,28,214],
                 [16,16,48,384],
                 [14,10,20,80,1800],
                 [14,10,12,20,320,4300],
                 [14,8,8,14,70,700,22000],
                 [14,4,4,14,48,180,1800,130000],
                 [14,4,4,6,22,122,900,10000,300000],
                 [10,4,4,6,12,36,380,1520,50000,2500000]]

traf = [0]*20

for i in range(20):
    k = rand(1, 80)
    while k in traf:
        k = rand(1, 80)

    traf[i] = k

n = int(input("Podaj ilosc typowanych liczb: "))

print(traf)

typo = [0]*n
for i in range(n):
    typo[i] = int(input("Podaj typowana liczbe: "))

w = 0
for i in range(n):
    if typo[i] in traf:
        w += 1

if w > 0:
    suma = multi_matryca[n-1][w]
    print(suma)
else:
    print("Lost")

