tel = {
    "Wika": 4758374,
    "Wadim": 7593740,
    "Liza": 8394739,
    "Tania": 3749374,
    "Alona": 3849263
}

tel["Wika"] = 8473940
tel["Alona"] = 3947394

del tel["Liza"]
for x, n in tel.items():
    print(x, n)

tel["Lena"] = 8749403
tel["Rafal"] = 9473048
sorted_tel = dict(sorted(tel.items()))
print("Sorted:")
for x, n in sorted_tel.items():
    print(x, n)

