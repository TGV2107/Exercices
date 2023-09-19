from math import *

class z:

    def __init__(self, num, denum) -> None:
        
        self.num = num
        
        self.denum = denum
        
        if self.num > 0:

            for i in range (2,self.num):

                if self.num%i == 0 and self.denum%i == 0:

                    self.num = self.num//i
                    self.denum = self.denum//i
        
        else:

            for i in range (-2,self.num, -1):

                if self.num%i == 0 and self.denum%i == 0:

                    self.num = self.num//i
                    self.denum = self.denum//i

    def __str__(self) -> str:
        
        return f"{self.num}/{self.denum}"
    
    def add(self,fraction2):
             
        num = (self.num * fraction2.denum) + (fraction2.num * self.denum)
        denum = self.denum * fraction2.denum
        
        return z(num,denum)

    def sub(self,fraction2):
        
        num = (self.num * fraction2.denum) - (fraction2.num * self.denum)
        denum = self.denum * fraction2.denum
        
        return z(num,denum)

    def mul(self,fraction2):

        num = self.num * fraction2.num
        denum = self.denum * fraction2.denum
        
        return z(num,denum)

    def div(self,fraction2):
    
        result = self.mul(z(fraction2.denum, fraction2.num))
        
        return z(result.num, result.denum)

    def cmp(self,fraction2):
        
        num1, num2 = (self.num * fraction2.denum), (fraction2.num * self.denum)

        if num1 > num2:

            return 1
        
        elif num1 < num2:

            return -1
        
        else:

            return 0



fraction = z(11,10)
fraction2 = z(12,10)

print(fraction.add(fraction2))
print(fraction.sub(fraction2))
print(fraction.mul(fraction2))
print(fraction.div(fraction2))
print(fraction.cmp(fraction2))