import os


class NoeudArbre:

    def __init__(self, nom, tableau_fils, nb_octets_fichier, nb_octets, nb_feuilles, nb_noeuds):

        self.nom = nom
        self.fils = tableau_fils
        self.nb_octets_fichier = nb_octets_fichier
        self.nb_octets = nb_octets
        self.nb_feuilles = nb_feuilles
        self.nb_noeuds = nb_noeuds
        self.hauteur = self.getHauteur()

    def getHauteur(self):

        if self.fils == []:
            return 0
        
        else:
            hauteurs = []
            for val in self.fils:
                hauteurs.append(val.getHauteur())
            return max(hauteurs) + 1
        
    def __str__(self) -> str:
        return self.nom
    
def fils(p):

    if os.path.isfile(p):
        return []
    return [(p+'/'+y) for y in os.listdir(p)]

def construit_arbre(p):

    fichiers_fils = [construit_arbre(y) for y in fils(p)]
    nb_octets_fichier = os.path.getsize(p)
    octets = nb_octets_fichier
    nb_noeuds = 1
    nb_feuilles = 0
    if fichiers_fils == []:
        nb_feuilles = 1
    for d in fichiers_fils:
        octets += d.nb_octets
        nb_noeuds += d.nb_noeuds
        if d.fils == []:
            nb_feuilles += 1
        else:
            nb_feuilles += d.nb_feuilles
    return NoeudArbre(p, fichiers_fils, nb_octets_fichier, octets, nb_feuilles, nb_noeuds)

arbre = construit_arbre("./TypesDeList")
print(fils(arbre.nom))
print(arbre.nb_feuilles, arbre.nb_octets, arbre.nb_octets_fichier, arbre.nb_noeuds)