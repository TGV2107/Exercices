import csv

HTAILLE = 100  # taille des tables de hachage
def hachage(cle):
    code = 0
    for car in cle:
        code += ord(car)
    return code % HTAILLE

#---
""""""
def creer_dico():
    return [None] * HTAILLE     # tableau de HTAILLE éléments

def ajouter_cle(dico, cle, valeur):
    h = hachage(cle)        # calculer le code de hachage de la clé
    if dico[h] == None:         # si l'entrée du dictionnaire est vide,
        dico[h] = [] # l'initialiser avec une liste vide
    # insérer la paire (cle, valeur) en tête de la liste des collisions
    dico[h].append((cle, valeur))
    return dico

def valeur_cle(dico, cle):
    h = hachage(cle)                        # calculer le code de hachage de la clé
    if dico[h] == None:                     # si l'entrée du dictionnaire est vide
        return None                         # None indique que la clé n'est pas présente
    for c, v in dico[h]:    # parcourir la liste des collisions
        if cle == c:                        # si la clé correspond
            return v                        # retourner la valeur
    return None                             # sinon la clé n'est pas dans le dictionnaire

def cles_dico(dico):
    t = []                                          # tableau des clés
    for liste in dico:                              # pour chaque élément du tableau
        if liste != None:                       # s'il n'est pas vide
            for cle, _ in liste:    # parcourir les collisions
                t.append(cle)                       # ajouter la clé
    return t                                        # retourner le tableau des clés

d = creer_dico()

with open("Dictionnaires et clés/Thomas/pop_dept.csv", encoding="utf8") as file:

    r = csv.reader(file)

    for row in r:

        département, population = row

        if population != "Population":
            population = int(population.replace(" ",""))
            d = ajouter_cle(d, département, population)

print(d)