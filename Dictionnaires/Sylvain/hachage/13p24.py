from Cours_hachage import*
import csv

with open("./pop_dept.csv") as f:
    data = []
    for ligne in csv.DictReader(f):
        ligne = dict(ligne)
        ligne["Département"] = str(ligne["Département"])
        ligne["Population"] = int(ligne["Population"])
        data.append(ligne)

print(data)
