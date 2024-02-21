class File:

    def __init__(self, length : int, values = []) -> None:
        
        assert length > 0, "La longueur maximale de la file doit être strictement supérieure à 0"

        self.values = [None] * length

        self.nextOut = 0
        self.nextIn = 0

        for val in values:
            self.enfiler(val)


    def enfiler(self, value):

        assert not self.isFull(), "La file est pleine"

        self.values[self.nextIn] = value
        self.nextIn += 1
        if self.nextIn == len(self.values): self.nextIn = 0


    def defiler(self):

        assert not self.isEmpty(), "La file est vide"

        value = self.values[self.nextOut]
        self.values[self.nextOut] = None

        self.nextOut += 1
        if self.nextOut == len(self.values): self.nextOut = 0

        return value
    
    
    def isEmpty(self) -> bool:

        return self.values[self.nextOut] == None
    
    
    def isFull(self):

        return self.values[self.nextIn] != None
    
    
    def head(self):

        return self.values[self.nextOut]
    
    
    def valuesToList(self) -> list:

        values = []

        for i in range(self.nextOut, len(self.values)):
            if self.values[i] != None : values.append(self.values[i])
            else: break
        
        for i in range(0, self.nextOut):
            if self.values[i] != None : values.append(self.values[i])
            else: break

        return values