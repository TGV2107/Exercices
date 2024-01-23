from lois import init_lois, nb_arrivees, nb_articles
from tpFiles import *

# coding: utf-8
#
# Squelette à compléter du programme de simulation de file d'attente
#
# L'état de la simulation est représenté par un tuple (caisse, file)
#   - caisse est le nombre d'articles du client courant restant à traiter par le caissier
#   - file est la file d'attente de la caisse. Chaque élément est le nombre d'articles du client
#
# La fonction simuler(npas, params) lance `npas` pas de simulation avec les paramètres `params`.
#   Elle appelle la fonction `intialiser`, puis `npas` fois la fonction `simuler_pas`
#   La fonction `simuler_pas` appelle `ajouter_clients` pour ajouter de nouveaux clients à la file,
#   puis `servir_client` pour traiter un article du client en cours (s'il y en a un)
#
# Il faut compléter les fonctions `intialiser`, `ajouter_clients` et `servir_clients`
#


# les paramètres de la simulation sont représentés par un dictionnaire
parametres = {
    'capacite': 20,     # longueur maximale de la file d'attente
    'flux': 0.8,        # nombre moyen de nouveaux clients par pas de temps
    'articles': 3       # nombre moyen d'articles par nouveau client
}

def afficher(horloge, sim):
    """ Afficher l'état de la simulation """
    caisse, file = sim
    print(str(horloge)+' caisse='+str(caisse)+' file='+str(elements_file(file)))

def initialiser(params):
    """ Initialiser les lois alátoires, la file et la caisse """
    #
    ### A COMPLETER ###
    #
    # retourner l'état initial de la simulation
    return (caisse, file)

def ajouter_clients(file):
    """ Ajouter de nouveaux clients, tant que la file n'est pas pleine """
    #
    ### A COMPLETER ###
    #
    # retourner la nouvelle file
    return file

def servir_client(caisse, file):
    """ Servir le client en cours, ou prendre le prochain client s'il y en a un """
    #
    ### A COMPLETER ###
    #
    # retourner le nouvel état de la simulation
    return (caisse, file)

def simuler_pas(sim):
    """ Exécuter un pas de la simulation sim et retourner le nouvel état """
    caisse, file = sim
    file = ajouter_clients(file)
    caisse, file = servir_client(caisse, file)
    # retourner le nouvel état de la simulation
    return (caisse, file)

def simuler(npas, params):
    """ Exécuter n pas de simulation """
    sim = initialiser(params)
    for horloge in range(npas):
        sim = simuler_pas(sim)
        afficher(horloge, sim)

# simulation en mode texte
simuler(100, parametres)

# simulation en mode graphique:
# commenter la ligne ci-dessus et décommenter les 2 lignes ci-dessous
# from visu import simuler_visu
# simuler_visu(initialiser, parametres, simuler_pas)