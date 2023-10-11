import csv

HTAILLE = 100  # taille des tables de hachage
def hachage(cle):
    code = 0
    for car in cle:
        code += ord(car)
    return code % HTAILLE

def creer_dico():
    return [None] * HTAILLE     # tableau de HTAILLE éléments

def ajouter_cle(dico, cle, valeur):
    global HTAILLE

    h = hachage(cle)        # calculer le code de hachage de la clé
    # insérer la paire (cle, valeur) en tête de la liste des collisions

    while dico[h] != None:
        if len(dico) ==  h+1:
            HTAILLE = HTAILLE + 1
            dico.append((cle,valeur))
            return dico

        h = h + 1

    dico[h] = (cle,valeur)

    return dico

def valeur_cle(dico, cle):
    h = hachage(cle)                        # calculer le code de hachage de la clé
    
    while h + 1 != len(dico):
        key, val = dico[h]
        if key == cle:
            return val
        h = h + 1

    return None

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