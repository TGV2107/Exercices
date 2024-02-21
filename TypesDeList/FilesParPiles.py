from ex25 import Pile


class File:

    def __init__(self) -> None:
        
        self.entree = Pile()
        self.sortie = Pile()


    def enfiler(self, val):
        
        self.entree.empiler(val)


    def defiler(self):
        
        if self.sortie.isVide():
            if self.entree.isVide(): return None
            for i in range(self.entree.taille()):
                self.sortie.empiler(self.entree.sommet())
                self.entree.depiler()
        
        res = self.sortie.sommet()
        self.sortie.depiler()
        return res
    
    
    def taille(self) -> int:

        return self.entree.taille() + self.sortie.taille()
    
    
    def head(self):

        if not self.sortie.isVide(): return self.sortie.sommet()
        if not self.entree.isVide(): return self.entree.values[0]
        return None
    
    
    def isEmpty(self) -> bool:

        return self.entree.isVide() and self.sortie.isVide()
    
    
    def elements(self) -> list:

        return list(self.sortie.elements() + self.entree.elements())