# coding: utf-8
#
# ==== Interface visualisant la file en temps réel
#   
# Il n'est pas nécessaire d'étudier le code de cette bibliothèque.
#
# La seule fonction destinée à être appelée est 
#   simuler_visu(init, params, simuler_pas)
# qui prend en paramètres
#       init : la fonction d'initialisation de la simulation
#       params : les paramètres de la simulation
#       simuler_pas : la fonction de simulation d'un pas
#
# Cette fonction affiche la simulation :
#   barre de gauche = nombre d'articles sur le tapis de caisse
#   barre grise = sépare la caisse de la file d'attente
#   barres bleues = nombres d'articles des clients en attente
#   barre noire = indique que le file est pleine
#
# Le bouton Start démarre la simulation, le bouton Stop l'arrête
# Les tirettes "flux" et "articles" changent les paramètres de la simulation.
# Ils prennent effet au prochain appui sur le bouton Start.
#

from nsi_ui import *

# -------- AJOUTS A LA BIBLIOTHEQUE NSI_UI --------

import nsi_ui as ui
_root = ui._root

# ======== HISTOGRAM ========

def _make_bar(parent, i, height, color):
    bar = tk.Frame(parent, width=15, height=height, background=color)
    bar.grid(row=1, column=i, padx=1, sticky='SW')
    return bar

def histogram(data, scale, color):
    """ Cree l'histogramme. """
    parent = tk.Frame(_root, height=200)
    parent.pack()

    bars = []
    for i in range(len(data)):
        bars.append(_make_bar(parent, i, scale*data[i], color))
    return (parent, bars, scale, color)

def update_histogram(histogram, data):
    parent, bars, scale, color = histogram
    reused = min(len(bars), len(data))
    for i in range(reused):
        bars[i].config(height=scale*data[i])
    if len(bars) > len(data):
        for i in range(len(data), len(bars)):
            bars[i].destroy()
        bars = bars[:len(data)]
    elif len(bars) < len(data):
        for i in range(len(bars), len(data)):
            bars.append(_make_bar(parent, i, scale*data[i], color))
    return (parent, bars, scale, color)

def set_bar_value(histogram, i, value):
    _, bars, scale, _ = histogram
    if i >= 0 and i < bars:
        bars[i].config(height=scale*value)

def set_bar_color(histogram, i, color):
    _, bars, scale, _ = histogram
    if i >= 0 and i < bars:
        bars[i].config(background=color)

def set_bar(histogram, i, value, color):
    _, bars, scale, _ = histogram
    if i >= 0 and i < bars:
        bars[i].config(height=scale*value, background=color)

#==== Le bouton Start-Stop

_running = False
_start = None
_step = None
_stop = None
_state = None
_delay = 100
_bstartstop = None

def _run_animation():
    """ Fonction executee par le thread """
    global _state
    _state = _step(_state)
    if _running:
        _root.after(_delay, _run_animation)

def _start_stop():
    """ Lance / arrete la simulation. """
    global _running, _state
    if _running:
        if _stop is not None:
            _stop(_state)
        _running = False
        _bstartstop.config(text="Start")
    else:
        if _start is not None:
            _state = _start()
        _running = True
        _bstartstop.config(text="Stop")
        _root.after(_delay, _run_animation)

def _single_step(ev):
    """ Effectue un pas d'animation si celle-ci est arretee """
    if not _running:
        global _state
        _state = _step(_state)

def start_stop_button(start, step, stop=None):
    """ Cree le bouton marche/arret.
        init est appelee sans parametres lorsque l'on demarre et doit retourner un etat
        step est appelee a chaque pas avec l'etat en parametre, et doir retourner le nouvel etat
        end est appellee avec l'etat en parametre lorsque l'on arrete
    """
    global _start, _step, _stop, _bstartstop
    # si le bouton a deja ete cree, ne pas le recreer
    _start = start
    _step = step
    _stop =stop
    if _bstartstop is not None:
        return _bstartstop
    _bstartstop = tk.Button(_root, text="Start", command=_start_stop)
    _bstartstop.pack(side=tk.LEFT)
    # avancer d'un pas si on tape espace
    _root.bind('<space>', _single_step)
    return _bstartstop

# -------- VISUALISTION DE LA FILE --------

from file_tableau import *

# Créer l'histogramme qui visualisera la simulation :
# première barre (verte) : articles restant à traiter par la caisse
# deuxième barre (grise) : séparation avec la file d'attente
# à partir de la troisieme barre (bleues) : nombre d'articles de chaque client en attente
# dernière barre (noire) : indique que la file est pleine
#
MAX_BAR = 20
h = histogram([0, MAX_BAR], 10, 'blue')
set_bar_color(h, 0, 'green')    # pour la caisse
set_bar_color(h, 1, 'grey')     # pour séparer de la file

def show_state(sim, capacite):
    """ Affiche l'état de la simulation par un histogramme """
    caisse, file = sim

    # créer un tableau des nombre d'articles des clients de la file d'attente
    data = []
    for articles in elements_file(file):
        data.append(articles)
    
    # créer les données de l'histogramme
    bars = [caisse, MAX_BAR] + data    # caisse, barre grise de séparation, file d'attente
    if file_pleine(file):
        bars.append(MAX_BAR) # barre noire pour montrer que la file est pleine

    # ajouter des barres vides
    bars = bars + [0]*(capacite - len(bars) + 3)

    # mettre à jour l'histogramme
    global h
    h = update_histogram(h, bars)  
    if file_pleine(file):
        set_bar_color(h, len(bars)-1, 'black')

def simuler_visu(init, params, simuler_pas):
    """ Initialiser l'interface de la simulation """
    capacite = params['capacite']

    def initialiser():
        """ initialiser la simulation avec les paramètres donnés """
        return init(params)

    def pas(sim):
        """ effectuer un pas et visualiser le nouvel état """
        sim = simuler_pas(sim)
        show_state(sim, capacite)
        return sim

    def changer_flux(f):
        params['flux'] = f

    def changer_articles(a):
        params['articles'] = a

    # le bouton start-stop
    start_stop_button(initialiser, pas)

    # les sliders pour les deux paramètres
    slider_flux = slider('flux', 0.2, 2.0, changer_flux)
    slider_articles = slider('articles', 1, 10, changer_articles)
    set_value(slider_flux, params['flux'])
    set_value(slider_articles, params['articles'])

    # état initial (pas très élégant...)
    global h
    h = update_histogram(h, [0, MAX_BAR, 0]+[0]*capacite)

    start_ui()
