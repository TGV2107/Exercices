def compte_inversion(tab : list):

    inversions = 0
    for i in range(0, len(tab)):
        for j in range(0, i):
            if tab[j] > tab[i]:
                inversions += 1

    return inversions

print(compte_inversion([2, 5, 1, 3]))