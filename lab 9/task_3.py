liga = set(["REAL MADRID", "BARCELONA", "MANCHESTER UNITED", "BAYERN MUNICH", "JUVENTUS", "LIVERPOOL", "MANCHESTER CITY", "ARSENAL", "CHELSEA", "PARIS SAINT GERMAIN"])
liga_2 = set(["TOTTENHAM", "BORUSSIA DORTMUND", "AC MILAN", "INTER MILAN", "ATLETICO MADRID", "AJAX", "PORTO", "AS ROMA", "OLYMPIQUE DE MARSEILLE", "GALATASARAY"])
liga_3 = set(["REAL MADRID", "BARCELONA", "ATLETICO MADRID", "MANCHESTER UNITED", "LIVERPOOL", "ARSENAL", "CHELSEA", "TOTTENHAM", "AJAX", "MANCHESTER CITY"])
liga_4 = set(["BORUSSIA DORTMUND", "BAYERN MUNICH", "PARIS SAINT GERMAIN", "INTER MILAN", "PORTO", "AS ROMA", "OLYMPIQUE DE MARSEILLE", "GALATASARAY", "JUVENTUS", "AC MILAN"])

#length check
liga_len = len(liga)
print(liga_len)

#deleting selected items
liga.discard("BARCELONA")
print(liga)

#compare
subset_check = liga <= liga_2
superset_check = liga_2 >= liga
print(subset_check)
print(superset_check)

#list conversions
list_1 = list(liga)
list_2 = list(liga_2)
print(list_1, list_2)