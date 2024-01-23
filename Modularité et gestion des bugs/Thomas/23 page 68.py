import random

import Objets.Thomas.NSI_2_page_46


def chifumi():
    choix = ["pierre","papier","ciseau"]

    while True:

        a, b = random.choice(choix), random.choice(choix)
        print(a,b)
        
        result = choix.index(a) - choix.index(b)

        if result == 1 or result == -2:

            return a
        
        elif result == -1 or result == 2:

            return b

print(chifumi())

# 1 ou - 2 : a a gagné, -1 ou 2, b a gagné