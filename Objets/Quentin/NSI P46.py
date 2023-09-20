from random import *

Carte_Valeurs = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi"]
class Carte:
    """Permet de créer une carte auquel on donne sa couleur et sa valeur"""

    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def getNom(self) -> str: return str(str(Carte_Valeurs[self.valeur - 1]) + " de " + self.couleur)


class Paquet:
    """Permet de créer un paquet de 52 cartes"""
    
    paquet = []
    for couleur in ["Pique", "Coeur", "Carreau", "Trèfle"]:
        for valeur in range(13):
            paquet.append(Carte(couleur, valeur + 1))

    def getCartes(self): return self.paquet

    def Tirer(self) -> Carte: return self.paquet[randint(0, len(self.paquet) - 1)]

paquet = Paquet()

for i in paquet.getCartes():
    print(i.getNom())
