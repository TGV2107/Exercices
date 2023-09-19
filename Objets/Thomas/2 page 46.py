from random import randint

import time

class Card:

    def __init__(self, Color, Value):

        self.Color = Color

        if Value > 10:
            
            Têtes = ["Valet","Dame","Roi"]

            Value = Têtes[Value-11]

        elif str(Value) == "1":

            Value = "As"

        self.Value = Value


    def getName(self):

        return str(self.Value) + " de " + self.Color

class Packet:

    def __init__(self):

        Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        Colors = ["Pique","Coeur","Carreau","Trèfle"]
        
        self.Cards = []

        for value in Values:

            for color in Colors:

                self.Cards.append(Card(color,value))

    def getRandomCard(self):

        return self.Cards[randint(0,len(self.Cards) - 1)]



Pack = Packet()

while True:

    print(Pack.getRandomCard().getName())

    time.sleep(1)