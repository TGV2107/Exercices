def texte(mots:list)->str:
    """
    Params :
    - mots : list
    
    returns 
    - phrase : str
    
    retoune une chaîne de caractere formé de la concaténation des éléments du tableau mots séparé par des espaces"""
    for element in mots:
        assert type(element) == str, "Au moins 1 des éléments de mots n'est pas une chaine de caractères"

    return " ".join(mots)

def enum(mots:list)->str:
    """
    Params :
    - mots : list
    
    Returns
    - phrase : str
    
    Retourne une chapine de caractère formé de la concaténation des éléments d'un tableau séparé par un espace sauf pour les 2 derniers élements séparé par un "et" """
    phrase = ""
    for element in mots:
        assert type(element) == str, "Au moins 1 des éléments n'est pas une chaîne de caractères"
        phrase = phrase + str(element) + " "
        return phrase [:len(phrase -2)]


