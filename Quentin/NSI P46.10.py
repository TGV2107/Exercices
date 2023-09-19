from turtle import *
from random import *

pen = Turtle()
pen.penup()
speed(0)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def dessiner(self):
        Dessin.croix((self.x, self.y))
    
class Segment:
    
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
    
    def dessiner(self):
        Dessin.trait((self.pos1.x, self.pos1.y), (self.pos2.x, self.pos2.y))

class Dessin:

    def croix(pos, l = 20):
        pen.penup()
        Dessin.trait(pos, [pos[0] + l + 1, pos[1] + l + 1])
        Dessin.trait([pos[0], pos[1] + l], [pos[0] + l, pos[1]])
        pen.penup()
    
    def trait(pos1, pos2):
        pen.penup()
        pen.goto(pos1)
        pen.pendown()
        pen.goto(pos2)
        pen.penup()

point = Point(0, 0)

for i in range(1000000000000000):
    p = Point(randint(-400, 400), randint(-400, 400))
    seg = Segment(point, p)
    seg.dessiner()
    p.dessiner()
    point = p

done()