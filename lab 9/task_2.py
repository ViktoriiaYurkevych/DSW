liga = set(["REAL MADRID", "BARCELONA", "MANCHESTER UNITED", "BAYERN MUNICH", "JUVENTUS", "LIVERPOOL", "MANCHESTER CITY", "ARSENAL", "CHELSEA", "PARIS SAINT GERMAIN"])
liga_2 = set(["TOTTENHAM", "BORUSSIA DORTMUND", "AC MILAN", "INTER MILAN", "ATLETICO MADRID", "AJAX", "PORTO", "AS ROMA", "OLYMPIQUE DE MARSEILLE", "GALATASARAY"])
liga_3 = set(["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "MANCHESTER UNITED", "LIVERPOOL", "ARSENAL", "CHELSEA", "TOTTENHAM", "AJAX", "MANCHESTER CITY"])
liga_4 = set(["BORUSSIA DORTMUND", "BAYERN MUNICH", "PARIS SAINT GERMAIN", "INTER MILAN", "PORTO", "AS ROMA", "OLYMPIQUE DE MARSEILLE", "GALATASARAY", "JUVENTUS", "AC MILAN"])

#Zwraca istniejące elementy w dwóch zestawach
intersection = liga.intersection(liga_2)
print(intersection)

#to get the difference between two sets
print(liga_2.difference(liga_3))
print(liga_3.difference(liga_2))

#Return a set that contains all items from both sets, duplicates are excluded
union = liga_2.union(liga_3)
print(union)

#Returns True if all elements of a set are present in another set
is_superset = liga_4.issuperset(liga)
print(is_superset)

#Returns True if all elements of a set are present in another set
is_subset = liga_2.issubset(liga)
print(is_subset)
