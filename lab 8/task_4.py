serniczkowy_spam = {}
i = 0
while True:
    answer = input("Czy chcesz otrzymac spam na maile? (tak czyli nie): ")
    if answer == "tak":
        user_mail = input("Wpisz swoje maile: ")
        serniczkowy_spam[i] = user_mail
        print("aktywowano")
    else:
        print("przykro")
        break
    i+=1

print(list(serniczkowy_spam.values()))