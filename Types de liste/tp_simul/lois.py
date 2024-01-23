# coding: utf-8
#
# ==== Fonctions statistiques pour les arrivées et le nombre d'articles
#
# Il n'est pas nécessaire d'étudier le code de cette bibliothèque.
#
# Les fonctions utiles sont :
#   - init_lois(moy_arrivees, moy_articles) qui intialise la bibliothèque
#       pour que les deux fonctions suivantes retournent en moyenne le
#       nombre d'arrivées et le nombre d'articles indiqués
#   - nb_arrivees() retourne un nombre d'arrivées aléatoire selon une loi dite Loi de Poisson
#   - nb_articles() retourne un nombre d'articles aléatoire selon une loi dite Loi Exponentielle
#

from random import random
from math import exp, factorial

def init_poisson(lambda_, n = 5):
    """ Calcule la fonction de répartition de la Loi de Poisson pour lambda donne et k = 1 à n"""
    cdf = [0.0] * n
    cumul = 0
    for k in range(len(cdf)):
        p = lambda_**k * exp(-lambda_) / factorial(k)
        cumul += p
        cdf[k] = cumul
    return cdf

def init_exp(mu, n = 50):
    """ Calcule la fonction de répartition de la Loi Exponentielle pour mu donne et k = 1 à n"""
    return [1 - exp(-mu * k) for k in range(n)]

def get_cdf(cdf):
    """ Donne une valeur aléatoire en fonction de la fonction de répartition cdf"""
    p = random()
    for i in range(len(cdf)):
        if cdf[i] > p:
            return i
    return len(cdf)

# fonctions exportées

def nb_arrivees():
    """ Retourne le nombre d'arrivées pendant un pas de temps.
        On utilise des arrivees poissonniennes.
    """
    assert poisson_cdf != None, "nb_arrivees: init_lois n'a pas été appelé !"
    return get_cdf(poisson_cdf)

def nb_articles():
    """ Retourne le nombre d'articles d'un client qui arrive à la file d'attente.
        Ce nombre suit une loi exponentielle.
    """
    assert exp_cdf != None, "nb_articles: init_lois n'a pas été appelé !"
    return 1 + get_cdf(exp_cdf)    # on veut au moins un article, d'où le 1+

poisson_cdf = None
exp_cdf = None

def init_lois(moy_arrivees, moy_articles):
    """ Initialise les distributions de probabilité """
    global poisson_cdf, exp_cdf
    poisson_cdf = init_poisson(moy_arrivees)
    exp_cdf = init_exp(1.0/moy_articles)
