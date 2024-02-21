class ArbreBin:

    def __init__(self, v=0, g = None, d = None) -> None:
        self.valeur = v
        self.fils_g = g
        self.fils_d = d

def hauteur(arbre):

    if arbre is None:
        return 0
    elif arbre.fils_g is None and arbre.fils_d is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.fils_g), hauteur(arbre.fils_d))
    

def pmax(a,v, prof = 1, maxi = 0):

    if a.valeur == v:
        maxi = prof

    return max([maxi, pmax(a.fils_g, v, prof + 1, maxi), pmax(a.fils_d, v, prof + 1, maxi)])


def pmax2(a,v):

    if a.fils_d == None and a.fils_g == None:
        if a.valeur ==v:
            return 1
        else:
            return 0
        
    else:
        if a.fils_g is not None: p_g = pmax2(a.fils_g,v)
        else: p_g = 0
        if a.fils_d is not None: p_d = pmax2(a.fils_d,v)
        else: p_d = 0

        if p_g > 0 or p_d > 0:
            return max(p_g, p_d) + 1
        elif a.valeur == v:
            return 1
        else:
            return 0
        
