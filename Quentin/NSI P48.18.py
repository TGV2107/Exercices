class Intervalle:
    """Représente un intervalle [min, max] avec min et max inclus ou exclus"""

    def __init__(self, min: float, isMinIn: bool, max: float, isMaxIn: bool):
        self.min = min
        self.isMinIn = isMinIn
        self.max = max
        self.isMaxIn = isMaxIn

    def __str__(self) -> str:
        return ("min: " + str(self.min) + " max: " + str(self.max))

    def isIn(self, value: float) -> bool:

        #Vérifie si value est dans l'intervalle et le return
        return (self.min < value and self.max > value) or (self.min == value and self.isMinIn == True) or (self.max == value and self.isMaxIn == True)

    def intersection(self, intervalle):
        """Renvoie l'intersection de 2 intervalles"""
        
        if self.min > intervalle.min:
            min = self.min
            isMinIn = self.isMinIn

        else:
            min = intervalle.min
            isMinIn = intervalle.isMinIn

        if self.min == intervalle.min and (self.isMinIn == False or intervalle.isMinIn == False):
            isMinIn = False


        if self.max > intervalle.max:
            max = self.max
            isMaxIn = self.isMaxIn

        else:
            max = intervalle.max
            isMaxIn = intervalle.isMaxIn

        if self.max == intervalle.max and (self.isMaxIn == False or intervalle.isMaxIn == False):
            isMaxIn = False

        return Intervalle(min, isMinIn, max, isMaxIn)

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

intervalle1 = Intervalle(0, False, 10, True)
intervalle2 = Intervalle(5, False, 50, False)

print(intervalle1.intersection(intervalle2))