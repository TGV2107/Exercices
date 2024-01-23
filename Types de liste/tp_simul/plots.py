# coding: utf-8
#
# ==== Fonctions pour afficher les statistiques
#
# Il n'est pas nécessaire d'étudier le code de cette bibliothèque.
#
# Les deux fonctions de cette bibliothèque sont les suivantes :
#
# - affiche_histogrammes prend en paramètres 4 tableaux
#   contenant les statistiques d'une série de simulations :
#       servis : nomnbre de clients servis
#       mecontents : nombre de clients mécontents (arrivés alors que la file était pleine)
#       libre : nombre de pas de temps où la caisse et la file d'attente étaient vides
#       longueur : longueur moyenne de la file d'attente
#   Elle affiche les 4 histogrammes représentant les distributions de ces valeurs
#
# - affiche_moyennes prend en paramètres 
#       - un tableau de valeurs d'un paramètre de la simulation et
#       - 4 tableaux contenant les moyennes d'une série de simulations
#         pour chaque valeur du paramètre :
#           servis : nomnbre moyen de clients servis
#           mecontents : nombre moyen de clients mécontents
#           libre : nombre moyen de pas de temps où la caisse était libre
#           longueur : moyenne des longueurs moyennes de la file d'attente
#   Elle affiche quatre courbes représentant l'évolution de ces statistiques
#   en fonction des valeurs du paramètre

import matplotlib.pyplot as plt

def affiche_histogrammes(servis, mecontents, libre, longueur):
    """ Affiche 4 histogrames montrant les distributions des resultats de multistats"""
    fig, axes = plt.subplots(ncols=4, figsize=(13,3))
    ax0, ax1, ax2, ax3 = axes.flatten()

    nbins = 20
    ax0.hist(servis, color='green', bins=nbins)
    ax0.set_title("Nombre de clients servis")

    ax1.hist(mecontents, color = 'red', bins=nbins)
    ax1.set_title("Nombre de clients mécontents")

    ax2.hist(libre, color = 'purple', bins=nbins)
    ax2.set_title("Durée caisse libre")

    ax3.hist(longueur, bins=nbins)
    ax3.set_title("Longueur moyenne de la file")

    plt.show()

def affiche_moyennes(parametres, servis, mecontents, libre, longueur):
    """ Affiche l'evolution des statistiques au cours d'une simulation"""
    fig, axes = plt.subplots(ncols=4, figsize=(13,3))
    ax0, ax1, ax2, ax3 = axes.flatten()

    ax0.plot(parametres, servis, color='green')
    ax0.set_title("Nombre de clients servis")
    ax0.set_ylim(bottom=0)

    ax1.plot(parametres, mecontents, color = 'red')
    ax1.set_title("Nombre de clients mécontents")
    ax1.set_ylim(bottom=0)

    ax2.plot(parametres, libre, color = 'purple')
    ax2.set_title("Durée caisse libre")
    ax2.set_ylim(bottom=0)

    ax3.plot(parametres, longueur)
    ax3.set_title("Longueur moyenne de la file")
    ax3.set_ylim(bottom=0)

    plt.show()
