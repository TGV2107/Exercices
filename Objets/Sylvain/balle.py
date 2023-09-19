class Projectile(): 

    def __init__(self,x,y,vy,vx) -> None:
        self.x = x
        self.y = y 
        self.vy = vy
        self.vx = vx

    def déplacement(self):
        self.vy = self.vy - g * dt
        self.x = self.x + dt * self.vx
        self.y = self.y + dt * self.vy
        
        return "x = " + str(self.x) + " y = "+ str(self.y) + " vy = " + str(self.vy) + " vx = " + str(self.vx)
        

dt = 20
g = 9.81

balle = Projectile(0,0,10,20)
print(balle.déplacement())
