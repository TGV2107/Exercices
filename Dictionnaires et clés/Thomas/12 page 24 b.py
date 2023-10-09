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