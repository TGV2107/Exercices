
def nb_diviseurs(j,n):

    if j == 1:
        return 1
    
    else:
        nb = nb_diviseurs(j-1, n)
        if n>j and n%j == 0:
            nb = nb + 1
        
    return nb


print(nb_diviseurs(6,12))