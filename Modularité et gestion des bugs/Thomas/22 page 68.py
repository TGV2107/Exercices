from matplotlib import pyplot


def barres(t : list):
    """Params :
    - t : list of float
    
    Returns :
    None
    
    Affiche les données du tableau t sous forme de barres verticales"""

    pyplot.bar(range(len(t)), t, width = 0.2, color = 'yellow', edgecolor = 'blue')
    pyplot.xticks(range(len(t)), ['Skill de Thomas', 'Skill de Quentin', 'C', 'D', 'E'], rotation = 45)
    pyplot.show()

def camembert(t):
    pyplot.pie(t, labels = ['Skill de Quentin', 'Skill de Thomas'])
    pyplot.legend()
    pyplot.show()

def graphe(x,y):
    pyplot.plot(x,y)
    pyplot.show()

camembert([1,50])