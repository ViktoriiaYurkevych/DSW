from random import randint as rand

orzel,reszka = 0,0

for i in range(50):
    a = rand(0,1)
    if a == 0:
        print("orzel")
        orzel += 1
    else:
        print("reszka")
        reszka += 1

print("orzel = ", orzel, ",reszka = ", reszka)