first_name = input('imię: ')
#Correcting the first letter to a capital letter
print(first_name.capitalize())

last_name= input('nazwisko: ')
#Correcting the first letter to a capital letter
print(last_name.capitalize())

number = input('numer telefonu: ')
#check if all characters are numbers
print(number.isdigit())
#to check if there are other characters besides digits,
#if there are, they are removed and a clean array is output
try:
    tmp = int(number)
    print('The number is correct')
except:
    print('Number incorrectly')
    #
s1 = "".join(c for c in number if  c.isdecimal())
print(s1)


number_2 = input('numer buta: ')
#check if all characters are numbers
print(number_2.isdigit())
#to check if there are other characters besides digits,
#if there are, they are removed and a clean array is output
try:
    tmp = int(number_2)
    print('The number is correct')
except:
    print('Number incorrectly')
    #
s1 = "".join(c for c in number_2 if c.isdecimal())
print(s1)





