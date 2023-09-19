class Tranche:

    def __init__(self, reflist : list, index0, index1) -> None:
        
        self.items = []

        self.reflist = reflist

        self.index0, self.index1 = index0, index1

        for i in range (self.index0, self.index1):

            self.items.append(reflist[i])