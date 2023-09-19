class Projectile:

    def __init__(self, x, y, vx, vy):

        self.x = x

        self.y = y

        self.vx = vx

        self.vy = vy

    def getX(self): return self.x

    def getY(self): return self.y

    def getVX(self): return self.vx

    def getVY(self): return self.vy

balle = Projectile(0,0,10,20)

def pas(balle, dt):

    for newballe in range (0,dt):

        