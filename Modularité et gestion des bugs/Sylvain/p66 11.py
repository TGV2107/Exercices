#
# Chapitre 3 - Exercice Newbie 11 - tinyurl
#

# Pour obtenir une URL courte du service tinyurl, il faut envoyer une requête
# à une URL de la forme http://tinyurl.com/api-create.php?url=<url_a_raccourcir>
# où <url_a_raccourcir> est remplacée par l'url
#
# Si l'attribut `OK` de la réponse est vrai,
# l'url raccourcie est dans l'attribut `text` de la réponse

import requests


# COMPLÉTER le code ci-dessous
def create_tinyurl(url):
    reponse = requests.get(...)
    if reponse.OK:
        ...
    ...

# TESTER la fonction ci-dessus
raccourci = create_tinyurl(...)
print(raccourci)

# COMPLÉMENT OPTIONNEL À L'EXERCICE
#
# Pour obtenir l'URL longue à partir de l'URL retournée par la fonction ci-dessus,
# il suffit de faire une requète à l'URL courte. Si la réponse est OK, l'URL
# d'origine est dans l'attribut `url` de la réponse :
def expand_tinyurl(tiny):
    reponse = requests.get(tiny)
    if reponse.ok:
        return reponse.url
    return 'erreur'

# TESTER qu'on retrouve bien l'URL de départ
print(expand_tinyurl(raccourci))