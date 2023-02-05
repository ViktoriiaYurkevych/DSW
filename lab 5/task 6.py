from random import randint

n = randint(1, 100)
print(n)

attempts = 3
while attempts > 0:
    a = int(input("Enter number:"))
    if a > n:
        print("Your number is more than hidden")
        attempts -= 1
        continue
    elif a < n:
        print("Your number is less than hidden")
        attempts -= 1
        continue
    elif a == n:
        print("Congratulations, You won!")
        break

if attempts == 0:
    print("You loose")
