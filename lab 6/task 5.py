x = int(input("Enter left border: "))
z = int(input("Enter right border: "))
n = int(input("Enter number of numbers: "))

l = []
for i in range(n):
    l.append(int(input("Enter number: ")))

print(l)
print("3rd from end element:", l[-3])

k = int(input("Enter number of deleted from end elements: "))
for i in range(k):
    l.pop()

print(l)

n2 = int(input("Enter number of numbers: "))

l2 = []
for i in range(n2):
    l2.append(int(input("Enter number: ")))

print(l2)
l3 = l + l2

print(l3)
dup = {}
for i in l3:
    if i in dup.keys():
        dup[i] += 1
    elif l3.count(i) > 1:
        dup[i] = 1

for i in dup:
    print("Element: ", i, ", times: ", dup[i])