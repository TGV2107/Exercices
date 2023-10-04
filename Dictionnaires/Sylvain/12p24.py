def creer_liste():
    """ Crée une liste vide (utilise un tuple vide) """
    return ()  # la liste vide est le tuple vide

def liste_vide(liste):
    """ Retourne True si la liste est vide """
    return liste == ()  # la liste est vide si c'est le tuple vide

def inserer(liste, element):
    """ Insère un élément en tête de liste et retourne la nouvelle liste """
    return (element, liste)  # nouvelle liste = tuple avec l'élément en tête

def tete(liste):
    """ Retourne la tête de liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "tete : liste vide !"
    return liste[0]  # la tête de liste est le premier élément du tuple

def queue(liste):
    """ Retourne la queue de la liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "queue : liste vide !"
    return liste[1]  # la queue de la liste est le deuxième élément du tuple

def elements_liste(liste):
    """ Retourne les éléments de la liste """
    res = []  # le tableau résultat
    while not liste_vide(liste):  # à chaque itération :
        res.append(tete(liste))  # ajouter la tête de liste au résultat
        liste = queue(liste)  # obtenir la nouvelle liste en enlevant la tête
    return res  # retourner le résultat

def taille(t):
    """ Retourne la taille de la liste """
    l = 0
    while not liste_vide(t):
        t = queue(t)
        l = l + 1
    return l


class Dico:
    def __init__(self):
        self.keys = creer_liste()
        self.values = creer_liste()

    def add_values(self, c, v):
        """ Opérateur qui associe la valeur v à la clé c dans le dictionnaire d """
        if c in elements_liste(self.keys):
            lc = elements_liste(self.keys)
            lv = elements_liste(self.values)
            for i in range(taille(self.keys)):
                if c == lc[i]:
                    lv[i] = v
        else:
            self.keys = inserer(self.keys, c)
            self.values = inserer(self.values, v)

    def access_values(self, c):
        """ Assesseur qui retourne la valeur associée à la clé C du dictionnaire
            dans le dictionnaire d """
        lc = elements_liste(self.keys)
        lv = elements_liste(self.values)
        for i in range(taille(self.keys)):
            if c == lc[i]:
                return lv[i]

    def element_dico(self):
        """ Itérateur qui retourne un tableau des clés d'un dictionnaire """
        return elements_liste(self.keys)


# Test
d = Dico()
print(elements_liste(d.keys), elements_liste(d.values))  # [] []

d.add_values("cle1", 1)
print(d.access_values("cle1"))  # 1
