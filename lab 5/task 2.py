n = int(input("Enter left border of diapason:"))
x = int(input("Enter right border of diapason:"))

i = 0
l = n
while l < x:
    print(l)
    i += 1
    l += 1
    type = int(input("Do you want to continue? (0 - no, 1 - yes)"))
    if type == 0 or i == 6:
        break;

print(min(range(n, l)))
print(max(range(n, l)))
print(sum(range(n, l))/len(range(n, l)))
print(sorted(range(n, l))[i//2])

