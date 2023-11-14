import random as r

def pcc():
    choix = ["papier", "caillou", "ciseau"]
    j1 = r.choice(choix)
    j2 = r.choice(choix)
    print(j1,j2)
    gagant_perdant = [('papier','caillou'),('ciseau','papier'),('caillou','ciseau')]
    if j1 == j2:
        return "Match nul"
    
    for c in gagant_perdant:
        if c == (j1,j2):
            return "Le joueur 1 a gagné"
    return "Le joueur 2 a gagné"

def poker():
    couleurs = ["pique","coeur","carreaux","trèfles"]
    numeros = ["1","2","3","4","5","6","7","8","9","valet","dame", "roi",'as']
    cartes = []
    while len(cartes)<5:
        choix_couleurs = r.choice(couleurs)
        choix_numeros = r.choice(numeros)
        #choix_cartes = (choix_numeros + " de " + choix_couleurs)
        choix_cartes = (choix_numeros, choix_couleurs)
        if not choix_cartes in cartes:
            cartes.append(choix_cartes)
    liste_valeurs = []
    for v,_ in cartes :
        liste_valeurs.append(v)
    d_valeur_occurence = {}
    for n in numeros:
        occuence = liste_valeurs.count(n)
        if not(n in d_valeur_occurence.keys()):
            d_valeur_occurence[n] = occuence
    liste_paires = []
    for n in d_valeur_occurence:
        if d_valeur_occurence[n] >= 2:
            liste_paires.append((n,d_valeur_occurence[n]))

    return cartes,liste_paires


        


result = poker()
print(result)



        
    

    





    