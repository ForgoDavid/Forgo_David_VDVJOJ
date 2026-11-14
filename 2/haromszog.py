
class Teglalap:
    info = "******************"

    def __init__(self, a_oldal, b_oldal):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def terulet(self):
        return self.a_oldal * self.b_oldal

    def kerulet(self):
        return (self.b_oldal + self.a_oldal) * 2


class Haromszog(Teglalap):
    def __init__(self, a_oldal, b_oldal):
        super().__init__(a_oldal, b_oldal)

    def terulet(self):
        return (self.a_oldal * self.b_oldal) / 2

    def kerulet(self):
        from math import sqrt
        return self.a_oldal + self.b_oldal + sqrt(self.a_oldal**2 + self.b_oldal**2)


harom = Haromszog(3, 4)
print(harom.terulet())
print(harom.kerulet())
print(harom.info)
