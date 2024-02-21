# coding: utf-8
#
# Chapitre 6 - Exercice Initié 38 - Inversions (page 134)
#

def fusion_et_inversions(l1, l2):
    """ fusionne deux listes l1 et l2 triées et renvoie :
    - la liste triée obtenue par la fusion
    - le nombre de paires (x1, x2) avec x1 dans l1 et x2 dans l2 telle que x1 > x2"""
    res = []
    i1, i2 = 0, 0  # indices pour parcourir l1, l2
    n = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            res.append(l1[i1])
            i1 += 1
            # A compléter
            print("1", i1, i2)
        else:
            res.append(l2[i2])
            i2 += 1
            print("2", i1, i2)
    while i1 < len(l1):
        # on a fini de parcourir l2
        res.append(l1[i1])
        # A compléter
    while i2 < len(l2):
        # on a fini de parcourir l1
        res.append(l2[i2])
        # A compléter
    return res, n


def tri_fusion_et_inversions(t):
    if len(t) <= 1:  # un tableau vide ou d'un seul élément est trié
        return t, 0
    else:  # diviser pour régner: on divise t en 2 parties égales
        t1 = []
        t2 = []
        i = 0
        while i < len(t) // 2:
            t1.append(t[i])
            i = i + 1
        while i < len(t):
            t2.append(t[i])
            i = i + 1
        t1, n1 = tri_fusion_et_inversions(t1)
        t2, n2 = tri_fusion_et_inversions(t2)
        t3, n3 = fusion_et_inversions(t1, t2)
        return  # A compléter


def nb_inversions(t):
    return tri_fusion_et_inversions(t)[1]


# Test:
print(nb_inversions([3, 5, 2]) == 2)
print(tri_fusion_et_inversions([4, 7, 2, 8, 1]) == ([1, 2, 4, 7, 8], 6))


#Question A : fichier ex 38
#Question B : quadratique, formule : n²
#Question C : 2nlog2(n) (réponse de cours)