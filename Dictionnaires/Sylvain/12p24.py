def creer_liste():
    """ CrÃ©e une liste vide """
    return ()               # la liste vide est le tuple vide

def liste_vide(liste):
    """ Retourne True si la liste est vide """
    return liste is ()      # la liste est vide si c'est le tuple vide

def inserer(liste, element):
    """ InsÃ¨re un Ã©lÃ©ment en tÃªte de liste et retourne la nouvelle liste """
    return (element, liste) # nouvelle liste = tuple avec l'Ã©lÃ©ment en tÃªte

def tete(liste):
    """ Retourne la tÃªte de liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "tete : liste vide !"
    element, _ = liste      # la tÃªte de liste est le 1er Ã©lÃ©ment du tuple
    return element

def queue(liste):
    """ Retourne la queue de la liste, ou produit une erreur si la liste est vide """
    assert not liste_vide(liste), "queue : liste vide !"
    _, reste = liste        # la queue de la liste est le 2e Ã©lÃ©ment du tuple
    return reste

def elements_liste(liste):
    """ Retourne les Ã©lÃ©ments de laliste """
    res = []                # le tableau rÃ©sultat
    while liste is not ():  # Ã  chaque itÃ©ration :
        tete, liste = liste #   extraire l'Ã©lÃ©ment et la nouvelle liste
        res.append(tete)    #   ajouter l'Ã©lÃ©ment au rÃ©sultat
    return res              # retourner le rÃ©sultat

def taille (t):
    return len(t)


class Dico: 
    def __init__(self) -> None:
        self.keys = []
        self.values = []
        
    
    def add_values(self,c,v):
        """Opérateur qui associe la valeur v à la clé c. dans le dictionnaire d"""
        if c in self.keys:
            lc = elements_liste(self.keys)
            lv = elements_liste(self.values)
            for i in range(taille(self.keys)):
                if c == lc[i]:
                    lv[i] = v
                    newlv = creer_liste()
                    for j in range(len(lv),0,-1):
                        val = lv[j]
                        if i == j:
                            val = v
                            inserer(newlv,val)
        else:
            inserer(self.keys,c)
            inserer(self.values,v)

        return self.keys,self.values


    def acces_values(self,c):
        """assesseur qui retourne la valeur associé a la clé C du dictionnaire
dans le dictionnaire d."""
        lc = elements_liste(self.keys)
        lv = elements_liste(self.values)
        for i in range(taille(self.keys)):
            if c == lc[i]:
                return lv[i]

    def element_dico(self)-> list:
        """ittérateur qui retroune un tableau des clés d'un dictionnaire d"""
        return elements_liste(self.keys)




    
    


                
        



    