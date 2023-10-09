from Cours_hachage import*
import csv

with open("./Dictionnaires/Sylvain/hachage/pop_dept.csv",encoding="utf8") as f:
    data = []
    for ligne in csv.reader(f):
        ligne = dict(ligne)
        print(ligne)
        ligne["Département"] = str(ligne["Département"])
        ligne["Population"] = int(ligne["Population"])
        data.append(ligne)

print(data)

"""r = csv.reader(f)
for row in r:
    dept,population = row
    """