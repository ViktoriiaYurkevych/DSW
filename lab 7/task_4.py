tup = ('one in two', 'two three x', 'four five then six', 'in', 'seven or eight no', 'nine in ten')

word = 'in'

if word in tup:
    print(tup.index(word))

num = 0

for x in tup:
    if word in x:
        num += 1

print(num)


