def texte(mots:list)->str:

    """Params :
    -mots : list of str
    
    Returns :
    - phrase : str
    
    Retourne une chaîne de caractères formée de la concaténation des éléments du tableau mots, séparés par des espaces"""

    sentence = mots.pop(0)

    for val in mots:
        assert type(val) == str, "Au moins un des éléments de mots n'est pas une chaîne de caractère"
        sentence = sentence + " " + val
    
    return sentence

print(texte(["a","b","djdojazdpjazopj"]))