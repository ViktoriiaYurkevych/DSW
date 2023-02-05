n = int(input("Enter number of numbers: "))
lst = []

for i in range(n):
    a = int(input("Enter number: "))
    lst.append(a)

max_element = max(lst)
print("Max element: ", max_element, ", times: ", lst.count(max_element))
