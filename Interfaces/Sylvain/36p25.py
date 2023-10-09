"""
def creer_ensemble()->dict: #Constructeur qui retourne un ensemble vide
    return {}

def elements_ensemble(e:dict)->dict: # Itérateur, qui retourne un tableau itérable contenant les éléments de l'ensemble e.
    return e.keys()

def appartientA(e:dict,v:float)-> bool : #Accesseur qui retourne Vrai si la veleur v appartient à l'ensemble e, Faux sinon.
    if v in elements_ensemble(e):
        return True
    return False

def ajouter_element(e:dict,v:float)->dict: #Opérateur qui ajoute la valeur à l'ensemble e.
    e[v] = True
    return e

def retirer_element(e:dict,v:float)-> dict: #Opérateur qui retire la valeur v de l'ensemble e.
    if appartientA(e,v) == True:
        e.pop(v)
    return e


def ensemble_vide(e:dict)-> bool: #Accesseur qui retourne vrai si la l'ensemble e est vide.
    if taille(e) == 0:
        return True
    return False

def taille(e:dict)->int: #Accesseur qui retourne le nb d'élements dans l'ensemble e.
    return len(e.keys())
"""
#c

def creer_ensemble()->list: #Constructeur qui retourne un ensemble vide
    return []

def elements_ensemble(e:list)->list: # Itérateur, qui retourne un tableau itérable contenant les éléments de l'ensemble e.
    return e

def appartientA(e:list,v:int)-> bool : #Accesseur qui retourne Vrai si la veleur v appartient à l'ensemble e, Faux sinon.
    return v in elements_ensemble(e)

def ajouter_element(e:list,v:int)->list: #Opérateur qui ajoute la valeur à l'ensemble e.
    if appartientA(e,v) == False:
        e.append(v)
    return e

def retirer_element(e:list,v:int)->list: #Opérateur qui retire la valeur v de l'ensemble e.
    if appartientA(e,v) == True:
        e.pop(v)
    return e


def ensemble_vide(e:list)-> bool: #Accesseur qui retourne vrai si la l'ensemble e est vide.
    if taille(e) == 0:
        return True
    return False

def taille(e:list)->int: #Accesseur qui retourne le nb d'élements dans l'ensemble e.
    return len(e)

#d

def union(e1,e2):
    """Opérateur qui retourne un ensemble étant l'union des ensembles A et B"""
    e = creer_ensemble()
    for i in elements_ensemble(e1):
        ajouter_element(e,i)
    for i in elements_ensemble(e2):
        ajouter_element(e,i)
    return e

def intersection(e1,e2): 
    """Opérateur qui retourne un ensemble étant l'intersection des ensembles A et B"""
    e = creer_ensemble()
    for i in elements_ensemble(e1):
        if appartientA(e2,i):
            ajouter_element(e,i)
    return e
    




