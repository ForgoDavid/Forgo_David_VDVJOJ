
class Szemely:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

    def bemutatkozas(self):
        print(f"Szia, a nevem {self.nev}, és {self.eletkor} éves vagyok.")


class Munkavallalo:
    def __init__(self, pozicio):
        self.pozicio = pozicio

    def munka(self):
        print(f"{self.pozicio} pozícióban dolgozom.")


class Dolgozo(Szemely, Munkavallalo):
    def __init__(self, nev, eletkor, pozicio):
        Szemely.__init__(self, nev, eletkor)
        Munkavallalo.__init__(self, pozicio)


dolgozo = Dolgozo("Anna", 30, "Programozó")
dolgozo.bemutatkozas()
dolgozo.munka()
