class dict:
    "Dictionnaire associant une clé à une valeur"

    def __init__(self, clés : list = [], valeurs : list = []) -> None:
        
        self.clés = clés

        self.valeurs = valeurs

    def add(self, key, value):
        
        if self.clés.__contains__(key):

            self.valeurs[self.clés.index(key)] = value

        else:

            self.clés.append(key)
            self.valeurs.append(value)

    def get(self,key):

        if not self.clés.__contains__(key):

            return None
        
        return self.valeurs[self.clés.index(key)]
    
    def keys(self):

        return self.clés #elements_liste(self.clés)
    

test = dict([1],[2])

print(test.keys(), test.clés, test.valeurs)

print(test.get(1))

test.add(4,6)

print(test.keys(), test.clés, test.valeurs)

test.add(4,7)

print(test.keys(), test.clés, test.valeurs)