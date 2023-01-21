A = tuple([2*i for i in range(100)])
print(A)

zero_pos = A.index(0)
sto_pos = A.index(100)

B = tuple([2*i+1 for i in range(100)])
print(B)

A += B
print(A)

print("Zero: miejsce w 1: ", id(zero_pos), ", miejsce w 2: ", id(A.index(0)))
print("Sto: miejsce w 1: ", id(sto_pos), ", miejsce w 2: ", id(A.index(100)))




