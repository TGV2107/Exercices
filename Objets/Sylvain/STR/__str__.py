
class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return  "(" + str(self.x) + "," + str(self.y) + ")"
        return f'({self.x},{self.y}'
    
p = Point(5,-66)
print(p)