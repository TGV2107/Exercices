def créer_ensemble():
    
    return {}

def elements_ensemble(e : dict):

    return e.keys()

def appartientA(e,v):

    if elements_ensemble(e).__contains__(v):

        return True
    
    return False

def ajouter_element(e,v):

    e[v] = None
    return e

def retirer_element(e : dict,v):

    if elements_ensemble(e).__contains__(v):
        e.pop(v)
    return e

def ensemble_vide(e):

    if taille(e) == 0:
        return True
    
    return False

def taille(e):

    return len(e)

def union(e,e2):
    
    newE = créer_ensemble()
    for val in elements_ensemble(e):
        ajouter_element(newE,val)
    for val in elements_ensemble(e2):
        ajouter_element(newE,val)
    return newE

def intersection(e,e2):

    newE = créer_ensemble()
    for val in elements_ensemble(e):
        if appartientA(e2,val) : ajouter_element(newE,val)

    return newE

ensemble = créer_ensemble()
print(ensemble)
print(ensemble_vide(ensemble))
ajouter_element(ensemble, 5)
print(ensemble)
print(ensemble_vide(ensemble))
ajouter_element(ensemble,10)
print(ensemble)
retirer_element(ensemble,5)
print(ensemble)
print(taille(ensemble))
print(appartientA(ensemble,5))
print(appartientA(ensemble,10))