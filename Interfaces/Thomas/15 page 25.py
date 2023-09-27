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

def setTaille(t, taille):

    if taille(t) > taille:

        newboard = créer_tableau(taille)
        for i in range (0, taille-1):
            set(newboard,t[i],i)

    elif taille(t) < taille:

        newboard = créer_tableau(taille)
        for i in range(0, taille(t) - 1):
            set(newboard,t[i],i)
    
    return newboard

while True:
    print("pepito")