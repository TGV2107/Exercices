import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

tableau = [1,2,5,4,3]
label = ["Adrien", "Thomas", "Sylvain", "Quentin","Marie"]

def barre(t:list):
    """Params :
    -t : liste float
    
    Returns : 
    None
    Affiche les données du tableau t sous frome d'une barre verticales"""
    plt.bar(range(len(t)), t, width = 0.5, color = 'red')
    plt.show()
    

def camembert(t:list,label:list)-> None:
    plt.figure(figsize = (5, 5))
    plt.pie(t, labels = label)
    plt.show()

def graphe(x:list, y:list):
    """Params :
    - x : liste de float, les abscisses
    - y : liste de float, les ordonées
    
    Returns : None
    Affiche un graphe avec les points (xi,yi)"""

    plt.plot(x,y,marker="x")
    plt.show()

graphe([1,2,4,5,6,7,9,10],[10,9,8,6,5,3,2,1])