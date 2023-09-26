def créer_tableau(taille):
    return [None]*taille

def set(t,v,i):

    if i <= taille(t) - 1:

        t[i] = v
        return t
    
    print("erreur")
    return None

def get(t,i):

    if i <= taille(t) - 1:
        return t[i]
    
    print("erreur")
    return None

def elements_tableau(t):
    return t

def tableau_vide(t):
    for val in t:

        if val != None:

            return False
        
    return True

def taille(t):
    return len(t)