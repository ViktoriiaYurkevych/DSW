from random import randint as rand

tup = tuple([rand(0, 10) for i in range(100)])

zero = 0
jeden = 0
dwa = 0

print(tup)

parz = []
nieparz = []

for elem in tup:
    if elem == 0:
        zero += 1
    elif elem == 1:
        jeden += 1
    elif elem == 2:
        dwa += 1

    if elem % 2 == 0:
        parz.append(elem)
    else:
        nieparz.append(elem)

print("zero: ", zero)
print("jeden: ", jeden)
print("dwa: ", dwa)
print("Parzyste:")
print(*parz, sep=', ')
print("Nieparzyste:")
print(*nieparz, sep=', ')








