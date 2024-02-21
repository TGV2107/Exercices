# coding: utf-8
#
# Chapitre 1 - Exercices Newbie (p.26)
# Implémentation d'une liste avec des tuples
#
# La liste est représentée par une tuple (tete, queue)
#   tete est le premier élément de la liste
#   queue est un tuple représentant le reste de la liste

def creer_liste():
    """ Crée une liste vide """
    return ()               # la liste vide est le tuple vide

def liste_vide(liste):
    """ Retourne True si la liste est vide """
    return liste == ()      # la liste est vide si c'est le tuple vide

def inserer(liste, element):
    """ Insère un élément en tête de liste et retourne la nouvelle liste """
    return (element, liste) # nouvelle liste = tuple avec l'élément en tête

def tete(liste):
    """ Retourne la tête de liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "tete : liste vide !"
    element, _ = liste      # la tête de liste est le 1er élément du tuple
    return element

def queue(liste):
    """ Retourne la queue de la liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "queue : liste vide !"
    _, reste = liste        # la queue de la liste est le 2e élément du tuple
    return reste

def elements_liste(liste):
    """ Retourne les éléments de laliste """
    res = []                # le tableau résultat
    while liste != ():  # à chaque itération :
        tete, liste = liste #   extraire l'élément et la nouvelle liste
        res.append(tete)    #   ajouter l'élément au résultat
    return res              # retourner le résultat


class Pile:

    def __init__(self, values = []) -> None:
        self.values = creer_liste()

        for val in values:
            self.empiler(val)
    
    def isVide(self):
        return liste_vide(self.values)
    
    def empiler(self, v):
        self.values = inserer(self.values, v)

    def depiler(self):
        self.values = queue(self.values)

    def sommet(self):
        return tete(self.values)
    
    def elements(self):
        return elements_liste(self.values)

    def taille(self):
        elements = Pile(values=self.elements())
        len = 0
        while  elements.isVide() == False:
            len = len + 1
            elements.depiler()
        return len
    
    def getElement(self, i):
        return self.elements()[i]
    
    def inverser(self):

        reversedPile = Pile()

        for i in range(self.taille()):
            reversedPile.empiler(self.sommet())
            self.depiler()
        
        self.values = reversedPile.values

"""class File():

    def __init__(self, taille, values = []) -> None:
        
        self.taille = taille

        self.values = [None] * taille

        for val in values:
            self.enfiler(val)

    def file_vide(self):
        return self.values[0] == None
    
    def enfiler(self, val):
        i = 0
        while self.values[i] != None:
            i = i + 1
            assert  not i == len(self.values), "La file est pleine"
        self.values[i] = val

    def defiler(self):
        val = self.values[0]
        newFile = []
        for i in range(1, len(self.values)):
            newFile.append(self.values[i])
        self.values = newFile
        self.values.append(None)
        return val
    
    def tête_file(self):
        if not self.file_vide:
            return self.values[0]
        else: return None"""


