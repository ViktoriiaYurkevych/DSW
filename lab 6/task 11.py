n = int(input("Enter number of numbers to generate: "))

lst = []
for i in range(n+1):
    lst.append(i)

lst[1] = 0

i = 2
while i <= n:
    if lst[i] != 0:
        j = i + i
        while j <= n:
            lst[j] = 0
            j = j+i

    i += 1

lst = set(lst)
lst.remove(0)
print(lst)