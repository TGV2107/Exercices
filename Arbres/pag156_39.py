# coding: utf-8
#
# Chapitre 7 - code d'arbres binaires utilisé dans de nombreux exercices (p152-157)
#


class ArbreBin:
    """
    Une implémentation minimaliste des arbre binaires.
    On peut juste construire des arbres, mais la classe ne contient pas d'autre méthode.
    Un arbre vide ne sera pas représenté par un élément de cette classe, mais pourra être représenté par None.
    """

    def __init__(self, v=0, g=None, d=None):
        self.valeur = v
        self.fils_g = g
        self.fils_d = d


class ABR:
    """
    Une implémentation des Arbres Binaires de Recherche.
    Implémente les ABR comme une hiérarchie d'objets de classe NoeudABR.
    La raison pour laquelle on 'encapsule' le noeud racine dans une classe ABR distincte
    est que l'objet None ne possède pas de méthodes (comme `insert` ou `recherche`).
    Avant d'utiliser ces méthodes sur un arbre il faudrait alors vérifier systématiquement  qu'il n'est pas vide, ce qui n'est pas pratique.
    En distinguant ABR de NoeudABR,
    on représente un arbre vide comme un ABR dont la racine est None.
    Il devient alors possible d'appliquer les méthodes sur tout objet de type ABR, qu'il soit vide ou pas.
    """

    def __init__(self, racine=None):
        self.racine = racine
        self.taille = self.get_taille(racine)

    def get_taille(self, noeux) -> int:

        if noeux == None:
            return 1
        else:
            return self.get_taille(noeux.fils_g) + self.get_taille(noeux.fils_d)

    def recherche(self, cle):
        """
        Suppose que l'arbre est organisé comme un ABR.
        Renvoie un NoeudABR correspondant à la clé, None s'il n'y en a pas
        """
        if self.racine is None:
            return None
        else:
            return self.racine.recherche(cle)

    def insere(self, cle):
        """
        Insère la clé dans une feuille de l'arbre, si elle n'est pas déjà présente dans l'arbre.
        Si la clé apparaît déjà dans l'arbre, l'arbre n'est pas modifié.
        Préserve la propriété des ABR : pour chaque noeud de l'arbre,
        - les clés présentes dans son sous-arbre gauche sont plus petites que la clé du noeud.
        - les clés présentes dans son sous-arbre droit sont plus grandes que la clé du noeud.
        """
        if self.racine is None:
            self.racine = NoeudABR(cle)
        else:
            self.racine.insere(cle)
        
        self.taille = self.get_taille(self.racine)
        


class NoeudABR:
    def __init__(self, c=0):
        # Il est assez logique de ne pas permettre dans le constructeur de définir fils_g et fils_d à autre chose que None,
        # car c'est la méthode insere qui est censé ajouter des noeuds.
        self.cle = c
        self.fils_g = None
        self.fils_d = None
        # on peut ajouter d'autres attributs

    def recherche(self, cle):
        """
        Suppose que l'arbre est un ABR.
        Renvoie un NoeudABR correspondant à la clé, None s'il n'y en a pas
        """
        if cle == self.cle:
            return self
        elif cle < self.cle and self.fils_g is not None:
            return self.fils_g.recherche(cle)
        elif cle > self.cle and self.fils_d is not None:
            return self.fils_d.recherche(cle)
        else:  # le sous-arbre où poursuivre la recherche est vide
            return None
        
    def recherche_it(self, cle):

        noeud = self
        while noeud != None and noeud.cle != cle:
            if cle < noeud.cle:
                noeud = noeud.fils_g
            else:
                noeud = noeud.fils_d
        return noeud
    
    def insere(self, c):
        """
        Insère la clé c dans une feuille sous un descendant du noeud, si elle n'y est pas déjà.
        Si la clé est déjà dans un descendant, l'arbre n'est pas modifié.
        Préserve la propriété des ABR : pour chaque noeud de l'arbre,
        - les clés présentes dans son sous-arbre gauche sont plus petites que la clé du noeud.
        - les clés présentes dans son sous-arbre droit sont plus grandes que la clé du noeud.
        """
        if c < self.cle:
            if self.fils_g is not None:
                self.fils_g.insere(c)
            else:
                self.fils_g = NoeudABR(c)
        elif c > self.cle:
            if self.fils_d is not None:
                self.fils_d.insere(c)
            else:
                self.fils_d = NoeudABR(c)


arbre = ABR(racine=NoeudABR(10))
arbre.insere(5)
arbre.insere(10)
print(arbre.taille)