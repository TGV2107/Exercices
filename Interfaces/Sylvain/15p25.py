def creer_tableau(taille:int) -> list:
    t = []
    for i in range(taille):
        t.append(None)
    return t

def set(t:list,v:int,i):
    if i <= taille(t):
        t[i] = v
        return t
    else:
        t1 = dynamique(t,i+1)
        t1[i] = v
        return t1
    

def get(t:list,i:int):
    
    if i <= taille(t):
        return t[i]
    print("Erreur : l'indice dépace dépasse la taille")
    return None

def elements_tableau(t:list):
    return t

def tableau_vide(t:list)-> bool:
    for i in elements_tableau(t):
        if i != None:
            return False
    return True

def taille(t):
    return len(t)

def dynamique(t:list,nt:int):
    t1 = creer_tableau(nt)
    for i in range(taille(t)):
        if i < nt:
            set(t1,get(t,i),i)
    return t1

t = [1,2,3,4,5]