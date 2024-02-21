"""
2,9,1,20,3
2,9     1,20,3
2   9     1,20    3
2   9     1   20   3
"""

def tri_fusion(tab : list) -> list:

    if len(tab) == 2:
        return [min(tab), max(tab)]
    
    else:
        sortedTab = []
        sorted1, sorted2 = [], []
        for i in range(0, len(tab)):
            if i <= len(tab)//2:
                sorted1.append(tab[i])
            else:
                sorted2.append(tab[i])
        sorted1 = tri_fusion(sorted1)
        sorted2 = tri_fusion(sorted2)
        