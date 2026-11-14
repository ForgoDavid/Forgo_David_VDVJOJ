
class Teglalap:
    szog = 90

    def __init__(self, a_oldal=5, b_oldal=10):
        self.a_oldal = a_oldal
        self.b_oldal = b_oldal

    def terulet(self):
        return self.a_oldal * self.b_oldal

    def kerulet(self):
        return self.a_oldal * 2 + self.b_oldal * 2
