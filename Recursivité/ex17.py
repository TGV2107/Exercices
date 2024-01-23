def calcul(n):

    if n%2==0:
        return n/2
    
    return 3*n + 1

def syracuse(n0, i):
    if i == 1:
        return calcul(n0)
    else:
        return syracuse(calcul(n0), i-1)

print(syracuse(3,2))

def vol(n0, turn = 0):

    if n0 == 1:
        return turn
    
    else:
        return vol(calcul(n0), turn = turn + 1)
    
print(vol(3))
