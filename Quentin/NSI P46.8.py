listeamitie = []
class Personne:
    """Permet de définir une personne par son nom et prénom"""
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Amis:
    """Permet de mettre en relation deux personnes"""
    def __init__(self, Personne1, Personne2):
        self.personne1 = Personne1
        self.personne2 = Personne2
        self.listepersonnes = [self.personne1, self.personne2]
    
    
    def ami(self, Personne):
        if Personne in self.listepersonnes:
            for p in self.listepersonnes:
                if Personne != p:
                    return p
        else:
            return None
        
class Groupe:
    """Permet de créer un groupe de personnes et y modifier les amitiés"""
    def __init__(self, listePersonne, listeAmis):
        self.listePersonnes = listePersonne
        self.listeAmis = listeAmis
    
    def addPersonne(self, personne):
        self.listePersonnes.append(personne)

    def amis(self, personne1, personne2):
        self.listeAmis.append(Amis(personne1, personne2))

a = Personne("A", "a")
b = Personne("B", "b")
c = Personne("C", "c")
d = Personne("D", "d")

listeamitie.append(Amis(a, b))
listeamitie.append(Amis(a, d))

for i in range(len(listeamitie)):
    if a in listeamitie[i].listepersonnes:
        print(listeamitie[i].ami(a).nom)