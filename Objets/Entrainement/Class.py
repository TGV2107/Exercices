
class caca:

    def __init__(self, Quentin : str, rien) -> None:
        

        self.Quentin = Quentin

        self.rien = rien

    def __str__(self) -> str:
        
        return ("La personne a pour atribut de quentin : "+ self.Quentin)
    
    def sertàrien(self):

        return self.rien
    


Sylvain = caca("noob",1)

print(Sylvain)

print(Sylvain.sertàrien())

Adrien = caca("puduq",Sylvain)

print(Adrien.rien)