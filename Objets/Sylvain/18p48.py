class Intervalle:
    """Représente un intervalle [min,max] avec a et b inclus ou exclus"""
    def __init__(self, min:float, max:float, isMinIn:bool, isMaxIn:bool):
        self.min = min
        self.max = max
        self.isMinIn, self.isMaxIn = isMinIn, isMaxIn
    
    def isIn(self,valeur:float)->bool:
        """Methode qui teste si la velur appartient à l'intervalle"""
        return (valeur > self.min and valeur < self.max) or (self.min == valeur and self.isMinIn == True) or (self.max == valeur and self.isMaxIn == True)

    
    def inter(self,in2):
        """Reveoie l'intersection de 2 intervalle"""
        if self.min > in2.min:
            min = self.min
            isMaxIn = self.isMaxIn
        else:
            min = in2.min
            isMinIn = in2.isMinIn
        if self.min == in2.min and (self.isMinIn == False or in2.isMinIn == False):
            isMinIn = False
        
        if self.max > in2.max:
            max = self.max
            isMaxIn = self.isMaxIn
        else:
            max = in2.max
            isMaxIn = in2.isMaxIn
        if self.max == in2.max and (self.isMaxIn == False or in2.isMaxIn == False):
            isMaxIn = False
        return Intervalle(min,max,isMinIn,isMaxIn)

        
    def union(self, intervalle):
                
        if self.min < intervalle.min:
            min = self.min
            isMinIn = self.isMinIn

        else:
            min = intervalle.min
            isMinIn = intervalle.isMinIn

        if self.min == intervalle.min and (self.isMinIn == False or intervalle.isMinIn == False):
            isMinIn = False


        if self.max < intervalle.max:
            max = self.max
            isMaxIn = self.isMaxIn

        else:
            max = intervalle.max
            isMaxIn = intervalle.isMaxIn

        if self.max == intervalle.max and (self.isMaxIn == False or intervalle.isMaxIn == False):
            isMaxIn = False

        return Intervalle(min, isMinIn, max, isMaxIn)
    
    def egal(self,in2):
        """teste si 2 intervalles sont égaux"""
        if self.min == in2.min and self.max == in2.max and self.isMinIn == in2.inMinIn and self.isMaxIn == in2.isMaxIn:
            return True
        else:
            return False
    
    def interNonVide(self,in2):
        intersection = self.inter(in2)
        if self.min == intersection.max and intersection.isMinIn == False and intersection.isMaxIn == False:
            return False
        else:
            return True

    def adjacent():
        pass

# Teste
intervalle1 = Intervalle(1,10,True, False)
print(intervalle1.isIn(5))
print(intervalle1.isIn(1))
print(intervalle1.isIn(10))
print(intervalle1.isIn(11))
i2 = intervalle1.union((Intervalle(5,15,True,True)))
print(i2.min,i2.max)
i3 = intervalle1.inter((Intervalle(5,15,True,True)))
print(i3.min,i3.max)

