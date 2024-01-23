class File:

    def __init__(self, t) -> None:
        
        self.values = [None] * t
        self.taille = 0

    def enfiler(self,v,p = False):

        assert not self.est_pleine(), "La file est pleine"

        if p:
            i  = 0
            while self.values[i] != None and self.values[i][1] == True:
                i += 1
            self.values.insert(i,(v,p))
            self.values.pop()

        else :
            self.values.insert(self.taille, (v,p))
            self.values.pop()

        self.taille += 1

    def defiler(self):

        self.values.append(None)
        self.taille -= 1
        return self.values.pop(0)
    
    def getTaille(self):

        return self.taille
    
    def elements(self):

        return self.values
    
    def est_vide(self):

        return self.taille() == 0
    
    def est_pleine(self):

        return self.getTaille() == len(self.values)