
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


class Kocka(Negyzet):
    def __init__(self, a_oldal):
        super().__init__(a_oldal)
        self.a_oldal = a_oldal

    def felszin(self):
        return self.terulet() * 6


koc = Kocka(7)
print(koc.terulet())
print(koc.felszin())
print(koc.info)
