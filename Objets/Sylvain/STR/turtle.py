from turtle import*

pen = Turtle()

class Points:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'( {self.x} , {self.y}'

class Segment:

    def __init__(self, a,b):
        self.pointa = a
        self.pointb = b
    
    def __str__(self) -> str:
        return f'[({self.pointa.x},{self.pointa.y},{self.pointb.x},{self.pointb.y})]'

class Dessin:

    def __init__(self,pen) -> None:
        self.pen = pen
    
    def trait(self,pa,pb):
        self.pen.penup()
        self.pen.goto(pa.x,pa.y)
        self.pen.pendown()
        self.pen.goto(pb.y,pb.y)
        self.pen.penup()

"""
    def croix(self.l=5):
        pen.penup()
        p1 = Points(point.x-1,point.y+1)
        p2 = Points(point.x+1,point.y+1)
        p3 = Points(point.x-1,point.y-1)
        p4 = Points(point.x+1,point.y-1)
        pen.goto(p1.x,p1.y)
        pen.penup()
        pen.goto(p4.x,p4.y)
        pen.pendown
        pen.pendown()
        pen.goto()
        x,y = points
        return x,y
"""
d = Dessin
p = Points(10,95)
segment = Segment(point,Points(4,5))

print(segment)
done()