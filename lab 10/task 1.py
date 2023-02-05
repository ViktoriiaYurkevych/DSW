
#lower, swapcase, capitalize

magic = "magia jest w opinii niektórych ucieleśnieniem Chaosu"
print(magic.lower())
print(magic.swapcase())
print(magic.capitalize())

#replace

s = "Magia jest w opinii niektórych ucieleśnieniem Chaosu"
s_new = s.replace('w opinii niektórych ucieleśnieniem Chaosu', 'zatem zemstą i orężem Chaosu')
print(s_new)


#lstrip, rstrip, reversed
mag ="****Ci, którzy uważają magię za Chaos, nie mylą się****"
print(mag.lstrip('*'))
print(mag.rstrip('*'))
print(list(reversed(mag)))

range_num = range(5, 9)
print(list(reversed(range_num)))

#count
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
count = random.count(('a', 'b'))
print("The count of ('a', 'b') is:", count)

#find
sea_str = 'Koniunkcji123Sfer'
print(sea_str.find('u'))

#isalnum

name = 'Wiedźmina123'
print(name.isalnum())
name_2 = 'Wiedźmina 123'
print(name_2.isalnum())

#startswith, endswith

text = "magia jest w opinii niektórych ucieleśnieniem Chaosu"
result = text.startswith('magia jest')
print(result)

result = text.startswith('jest w opinii', 7, 18)
print(result)

result = text.endswith('ucieleśnieniem')
print(result)




