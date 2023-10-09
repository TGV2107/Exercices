class Personne:

    def __init__(self, Nom, Prenom):
        
        self.Nom = Nom

        self.Prenom = Prenom

class Amis:

    def __init__(self, Personne1 : Personne(), Personne2 : Personne()):
        
        self.Personne1 = Personne1

        self.Personne2 = Personne2
    
    def ami(self, PersonneAmis):

        if PersonneAmis == self.Personne1:

            return self.Personne2
        
        elif PersonneAmis == self.Personne2:

            return self.Personne1
        
        else:  return None

class Groupe:

    def __init__(self, Personnes : list, AmisList) -> None:
        
        self.Personnes = Personnes

        self.Amis = AmisList

    def addPersonne(self, Personne):

        self.Personnes.append(Personne)
        
    def addAmis(self, Personne1, Personne2):

        if self.Personnes.__contains__(Personne1) and self.Personnes.__contains__(Personne2):
            
            Relation = Amis(Personne1, Personne2)

            self.Amis.append(Relation)
        
    def getAmis(self, Personne):

        amis = []

        for Relation in self.Amis:

            if Relation.Personne1 == Personne:

                amis.append(Relation.Personne2)

            elif Relation.Personne2 == Personne:

                amis.append(Relation.Personne1)
            
        return amis



Thomas = Personne("Guntzer Vetter", "Thomas")
print(Thomas.Nom)
Quentin = Personne("Beyl", "Quentin")
Sylvain = Personne("Rhin","Sylvain")
print(Thomas.Nom)
print(Quentin.Prenom)

amitiétest = Amis(Thomas,Quentin)
print(amitiétest.Personne1.Nom)

groupe = Groupe([],[])

groupe.addPersonne(Thomas)
groupe.addPersonne(Quentin)
groupe.addPersonne(Sylvain)

groupe.addAmis(Thomas,Quentin)
groupe.addAmis(Thomas,Sylvain)

#for ami in groupe.getAmis(Thomas):

    #print(ami.Nom, ami.Prenom)