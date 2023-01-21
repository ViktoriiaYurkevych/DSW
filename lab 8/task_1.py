menu = {
    "pizza": 15,
    "zupa": 10,
    "kawa": 16,
    "herbata": 15,
    "chleb": 5
}

menu["pizza hawajska"] = 19
for x, n in menu.items():
    print(x, n)

key_max = max(menu.keys(), key=(lambda k: menu[k]))
key_min = min(menu.keys(), key=(lambda k: menu[k]))

print(key_min, ',', key_max)

del menu[key_max]
del menu[key_min]

for x, n in menu.items():
    print(x, n)