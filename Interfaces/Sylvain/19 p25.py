def creer_tableau(taille:int) -> list:
    t = []
    for i in range(taille):
        t.append(None)
    return t

def changer_taille(t:list,nt):
    diff = abs(len(t)-nt)
    for i in range(diff):
        if len(t) > nt:
            t.pop()
        if len(t) < nt:
            t.append(None)
    return t

tableau = creer_tableau(6)
t1 = [3,4,6,4,3,3] 
print(changer_taille(t1, 4))
print(changer_taille(t1, 10))


