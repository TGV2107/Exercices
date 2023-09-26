def créer_tableau(taille):
    return [None]*taille

def set(t,v,i):
    t[i] = v
    return t

def get(t,i):
    return t[i]

def elements_tableau(t):
    return t

def tableau_vide(t):
    for val in t:

        if val != None:

            return False
        
    return True

def taille(t):
    return len(t)