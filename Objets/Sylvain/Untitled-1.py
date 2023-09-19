from random import*
class Carte:
    """c'est une classe qui défini une carte avec sa valeur et sa couleur"""

    def __init__(self,color,valeur) -> None:
        self.valeur = valeur
        self.color = color

    def name(self):
        if self.valeur == 11:
            nom = "valet"
        elif self.valeur == 12:
            nom = "dame"
        elif self.valeur == 13:
            nom = "roi"
        elif self.valeur == 1:
            nom = "as"
        else:
            nom = str(self.valeur)
        return nom + " de " + self.color

    def tirer(self):
        self.valeur = randint(1,14)

        self.color = choice["pique", "coeur","trêfle","carreau"]

class Paquet:
    def __init__(self) -> None:
        self.nb = 52
        
    
    def creer(self):
        couleur = ["pique", "coeur","trêfle","carreau"]
        listecarte = []
        for i in couleur:
            for k in range(1,13):
                listecarte.append((i,k))
        return listecarte
                
        
    
    def tirer(self,listecarte):
        choosecarte = listecarte[randint(0,51)]
        return choosecarte

carte1 = Carte("Pique", 1)
print(carte1.name())

paquet1 = Paquet()

choicecarte = paquet1.tirer(paquet1.creer())
couleur, valeur = choicecarte
carte2 = Carte(couleur, valeur)
print(carte2.name())