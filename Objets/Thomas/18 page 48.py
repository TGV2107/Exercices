class Intervalle:

    def __init__(self, min : float, max : float, isMinIn : bool, isMaxIn : bool) -> None:
        
        self.min, self.max = min, max
        self.isMinIn, self.isMaxIn = isMinIn, isMaxIn
    
    def __str__(self) -> str:
        
        if self.isMinIn == False:

            strMin = "]"
        else:

            strMin = "["
        
        if self.isMaxIn == False:

            strMax = "["
        else:

            strMax = "]"
        
        return f'{strMin}{self.min};{self.max}{strMax}'

    def isIn(self,value):

        if value > self.min and value < self.max: return True
        
        elif (value == self.min and self.isMinIn == True) or (value == self.max and self.isMaxIn == True): return True
        
        return False
    
    def intersection(self, intervalle2):

        if self.min > intervalle2.min:

            min = self.min
            isMinIn = self.isMinIn

        else:

            min = intervalle2.min
            isMinIn = intervalle2.isMinIn

        if self.max < intervalle2.max:

            max = self.max
            isMaxIn = self.isMaxIn

        else:

            max = intervalle2.max
            isMaxIn = intervalle2.isMaxIn
        

        if (self.min == intervalle2.min) and (self.isMinIn == False or intervalle2.isMinIn == False):
                
            isMinIn = False
        
        if (self.max == intervalle2.max) and (self.isMaxIn == False or intervalle2.isMaxIn == False):

            isMaxIn == False

        return Intervalle(min, max, isMinIn, isMaxIn)
    
    def union(self, intervalle2):

        if self.min < intervalle2.min:

            min = self.min
            isMinIn = self.isMinIn

        else:

            min = intervalle2.min
            isMinIn = intervalle2.isMinIn

        if self.max > intervalle2.max:

            max = self.max
            isMaxIn = self.isMaxIn

        else:

            max = intervalle2.max
            isMaxIn = intervalle2.isMaxIn
        

        if (self.min == intervalle2.min) and (self.isMinIn == True or intervalle2.isMinIn == True):
                
            isMinIn = True
        
        if (self.max == intervalle2.max) and (self.isMaxIn == True or intervalle2.isMaxIn == True):

            isMaxIn == True

        return Intervalle(min, max, isMinIn, isMaxIn)
    
    def isEgal(self, i):
        
        if self.min == i.min and self.max == i.max and self.isMinIn == i.isMinIn and self.isMaxIn == i.isMaxIn:
            
            return True
        
        else: return False

    def interNonVide(self):
        pass

    def adjacent(self):
        pass

inter = Intervalle(0,10, False, True)

print(inter.isIn(5))
print(inter.isIn(0))
print(inter.isIn(10))
print(inter.isIn(11))

print(inter.intersection(Intervalle(5,15,True,True)))

print(inter.union(Intervalle(5,15,True,True)))