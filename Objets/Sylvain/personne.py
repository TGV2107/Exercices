class Personne: 
    """Défini le nom et le prénom d'une personne"""
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
class Amis:
    def __init__(self,ami1,ami2):
        self.ami1 = ami1
        self.ami2 = ami2
    
    def ami(self,p):
        liste = [self.ami1,self.ami2]
        for ami in liste:
            if p == ami:
                liste.remove(p)
                return liste[0]
        else:
            return None

    
class Groupe:

    def __init__(self,lp,la):
        self.lp = lp
        self.la = la

    def addpeople(self,person):
        """Ajoute la personne à la liste des personnes du groupe si elle n'y est pas déjà"""
        if person not in self.lp:
            return self.lp.append(person)
        else:
            return None
        
    def addfriends(self,friend, p1, p2):
        if not(p1 in self.lp and p2 in self.lp):
            print("au moins une des 2 personnes ne fait pas parti du groupe")
            if not(p1 in self.lp):
                self.lp.append(p1)
            if not(p2 in self.lp):
                self.lp.append(p2)
        return self.la.append(Amis(p1,p2))
    
    def chercher(self,personne):
        "retourne une liste donnant les amis de la personne p"
        if personne in self.la:
            listeamis = []
            for a in self.la:
                if a.p1 == p:
                    listeamis.append(a.p1)
                elif a.p2 == p:
                    listeamis.app
                    
            return listeamis
        return personne + " n'as pas d'amis dans ce groupe"
                
#teste
Personne1 = Personne("Beyl","Quentin")
personne2 = Personne("A","B")
personne3 = Personne("Markert", "Arnaud")
personne4 = Personne("RIHN","Sylvain")
print(personne2.nom + " " + personne2.prenom)
print(Personne1.nom + " " + Personne1.prenom)

amitier = Amis(personne2,Personne1)
print(amitier.ami(personne2)).__str__

groupe1 = Groupe([Personne1,personne2,personne3], [amitier])
groupe1.addfriends(personne4,Personne1,personne2)
for p in groupe1.lp:
    print(p.prenom)
groupe1.addfriends(personne3,personne4)
for a in groupe1.la:
    print(a.p1.prenom,a.p2.prenom)

print(groupe1.chercher(personne4))

listeAmisDeCoralie = groupe1.chercher(personne4)
for i in listeAmisDeCoralie:
    print(p.prenom)