n = int(input("Enter number of numbers:"))

i = 0
while i < n:
    a = int(input("Enter number: "))
    if -6 <= a <= 6:
        print("in diapason [-6;6]")
    else:
        print("not in diapason [-6;6]")
    i += 1

