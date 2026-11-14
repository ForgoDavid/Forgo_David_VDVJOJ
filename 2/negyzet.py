
class Teglalap:
    info = "******************"

    def __init__(self, a_oldal, b_oldal):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def terulet(self):
        return self.a_oldal * self.b_oldal

    def kerulet(self):
        return (self.b_oldal + self.a_oldal) * 2


class Negyzet(Teglalap):
    def __init__(self, a_oldal, b_oldal=0):
        super().__init__(a_oldal, b_oldal)
        self.a_oldal = a_oldal
        self.b_oldal = a_oldal


n = Negyzet(7)
print(n.terulet())
print(n.kerulet())
print(n.info)
