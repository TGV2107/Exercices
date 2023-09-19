class Z:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num + "/" + self.den)

    def add(self, fraction2):
        