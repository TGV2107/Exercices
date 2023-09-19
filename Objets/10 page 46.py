from turtle import *
from random import randint

class Point:

    def __init__(self, x, y) -> None:
        
        self.x, self.y = x, y


class Segment:

    def __init__(self, p1, p2) -> None:
        
        self.p1, self.p2 = p1, p2

class Dessin():

    def trait(self, p1 : Point(), p2 : Point()):

        penup()
        goto(p1.x, p1.y)
        pendown()
        goto(p2.x, p2.y)
        penup()

    def Croix(self, p1, longueur):
                                                                                            
        pass


drawn = Dessin()
drawn.trait(Point(1,2),Point(2,3))



# pour faire une suite de points reliés les uns après les autres :

"""
oldP = #point à remplacer
for i in rane (50):
    p = point(randint(-400,400), randint(-400,400))
    seg = Segment(oldP, p)
    seg.dessiner (d, t)
    p.dessiner(d,t)
    oldP = p
"""